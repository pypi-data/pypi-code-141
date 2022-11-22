import pytest
from steamship_tests.utils.fixtures import get_steamship_client
from steamship_tests.utils.random import random_index, random_name

from steamship import SteamshipError
from steamship.base import TaskState
from steamship.data.embeddings import EmbeddedItem

_TEST_EMBEDDER = "test-embedder"


def test_create_index():
    client = get_steamship_client()

    index_handle = random_name()
    index = client.use_plugin(
        "embedding-index",
        index_handle,
        config={"embedder": {"plugin_handle": _TEST_EMBEDDER, "fetch_if_exists": True}},
        fetch_if_exists=False,
    )

    assert index is not None

    # Duplicate creation should fail with fetch_if_exists=False
    with pytest.raises(SteamshipError):
        index = client.use_plugin(
            "embedding-index",
            index_handle,
            config={"embedder": {"plugin_handle": _TEST_EMBEDDER, "fetch_if_exists": True}},
            fetch_if_exists=False,
        )

    # Duplicate creation should fail with fetch_if_exists=False for embedder
    with pytest.raises(SteamshipError):
        index = client.use_plugin(
            "embedding-index",
            index_handle,
            config={"embedder": {"plugin_handle": _TEST_EMBEDDER, "fetch_if_exists": False}},
            fetch_if_exists=True,
        )

    index.delete()


def test_reload_and_delete_index():
    steamship = get_steamship_client()
    index = steamship.use_plugin(
        "embedding-index",
        random_name(),
        config={"embedder": {"plugin_handle": _TEST_EMBEDDER, "fetch_if_exists": True}},
        fetch_if_exists=True,
    )
    assert index.id is not None

    index2 = steamship.use_plugin(
        "embedding-index",
        index.handle,
        config={"embedder": {"plugin_handle": _TEST_EMBEDDER, "fetch_if_exists": True}},
        fetch_if_exists=True,
    )

    assert index.id == index2.id
    index.delete()

    # Having deleted it, the ID should now be different
    index3 = steamship.use_plugin(
        "embedding-index",
        index.handle,
        config={"embedder": {"plugin_handle": _TEST_EMBEDDER, "fetch_if_exists": True}},
        fetch_if_exists=True,
    )
    assert index.id != index3.id
    index3.delete()


def _list_equal(actual, expected):
    assert len(actual) == len(expected)
    assert all([a == b for a, b in zip(actual, expected)])


def test_insert_many():
    steamship = get_steamship_client()
    with random_index(steamship, _TEST_EMBEDDER) as index:
        item1 = EmbeddedItem(
            value="Pizza", external_id="pizza", external_type="food", metadata=[1, 2, 3]
        )
        item2 = EmbeddedItem(
            value="Rocket Ship",
            external_id="workspace",
            external_type="vehicle",
            metadata="Foo",
        )

        index.index.insert_many([item1, item2])
        index.index.embed().wait()

        list_response = index.index.list_items()
        assert len(list_response.items) == 2
        assert len(list_response.items[0].embedding) > 0
        assert len(list_response.items[1].embedding) > 0
        assert len(list_response.items[0].embedding) == len(list_response.items[1].embedding)

        res = index.index.search(item1.value, include_metadata=True, k=100)
        res.wait()
        items = res.output.items
        assert items is not None
        assert len(items) == 2
        assert items[0].value.value == item1.value
        assert items[0].value.external_id == item1.external_id
        assert items[0].value.external_type == item1.external_type
        _list_equal(items[0].value.metadata, item1.metadata)

        res = index.index.search(item2.value, include_metadata=True)
        res.wait()
        items = res.output.items
        assert items is not None
        assert items[0].value.value == item2.value
        assert items[0].value.external_id == item2.external_id
        assert items[0].value.external_type == item2.external_type
        assert items[0].value.metadata == item2.metadata


def test_embed_task():
    steamship = get_steamship_client()
    with random_index(steamship, _TEST_EMBEDDER) as index:
        _ = index.index.insert("test", reindex=False)
        res = index.index.embed()

        assert res.task_id is not None
        assert res.state is not None
        assert res.task_created_on is not None
        assert res.task_last_modified_on is not None
        assert res.state == TaskState.waiting
        res.wait()
        assert res.state == TaskState.succeeded


def test_duplicate_inserts():
    steamship = get_steamship_client()
    with random_index(steamship, _TEST_EMBEDDER) as index:
        # Test for suppressed re-indexing
        a1 = "Ted can eat an entire block of cheese."
        q1 = "Who can eat the most cheese"
        _ = index.index.insert(a1)
        _ = index.index.search(q1)


def test_index_usage():
    steamship = get_steamship_client()
    with random_index(steamship, _TEST_EMBEDDER) as index:
        a1 = "Ted can eat an entire block of cheese."
        q1 = "Who can eat the most cheese"
        _ = index.index.insert(a1)
        _ = index.index.search(q1)

        # Now embed
        task = index.index.embed()
        task.wait()
        assert task.state == TaskState.succeeded

        search_results = index.index.search(q1)
        search_results.wait()
        search_results = search_results.output.items
        assert len(search_results) == 1
        assert search_results[0].value.value == a1

        # Associate metadata
        a2 = "Armadillo shells are bulletproof."
        q2 = "What is something interesting about Armadillos?"
        a2id = "A2id"
        a2type = "A2type"
        a2metadata = {
            "id": a2id,
            "idid": f"{a2id}{a2id}",
            "boolVal": True,
            "intVal": 123,
            "floatVal": 1.2,
        }

        _ = index.index.insert(a2, external_id=a2id, external_type=a2type, metadata=a2metadata)
        search_results2 = index.index.search(q2)
        search_results2.wait()
        search_results = search_results2.output.items
        assert len(search_results) == 1
        assert search_results[0].value.value == a2
        assert search_results[0].value.external_id is None
        assert search_results[0].value.external_type is None
        assert search_results[0].value.metadata is None

        search_results3 = index.index.search(q2, include_metadata=True)
        search_results3.wait()
        search_results = search_results3.output.items
        assert len(search_results) == 1
        assert search_results[0].value.value == a2
        assert search_results[0].value.external_id == a2id
        assert search_results[0].value.external_type == a2type

        assert search_results[0].value.metadata == a2metadata
        # Because I don't know pytest enough to fully trust the dict comparison..
        assert search_results[0].value.metadata["id"] == a2id
        assert search_results[0].value.metadata["idid"] == f"{a2id}{a2id}"

        search_results4 = index.index.search(q2, k=10)
        search_results4.wait()
        search_results = search_results4.output.items
        assert len(search_results) == 2
        assert search_results[0].value.value == a2
        assert search_results[1].value.value == a1


def test_multiple_queries():
    steamship = get_steamship_client()
    with random_index(steamship, _TEST_EMBEDDER) as index:
        # Test for suppressed re-indexing
        a1 = "Ted can eat an entire block of cheese."
        a2 = "Joe can drink an entire glass of water."
        _ = index.index.insert_many([a1, a2])
        index.index.embed().wait()

        qs1 = ["Who can eat the most cheese", "Who can run the fastest?"]
        search_results = index.index.search(qs1)
        search_results.wait()
        search_results = search_results.output
        assert len(search_results.items) == 1
        assert search_results.items[0].value.value == a1
        assert search_results.items[0].value.query == qs1[0]

        qs2 = ["Who can tie a shoe?", "Who can drink the most water?"]
        search_results = index.index.search(qs2)
        search_results.wait()
        search_results = search_results.output
        assert len(search_results.items) == 1
        assert search_results.items[0].value.value == a2
        assert search_results.items[0].value.query == qs2[1]

        qs3 = ["What can Ted do?", "What can Sam do?", "What can Jerry do?"]
        search_results = index.index.search(qs3)
        search_results.wait()
        search_results = search_results.output
        assert len(search_results.items) == 1
        assert search_results.items[0].value.value == a1
        assert search_results.items[0].value.query == qs3[0]

        qs3 = ["What can Sam do?", "What can Ted do?", "What can Jerry do?"]
        search_results = index.index.search(qs3)
        search_results.wait()
        search_results = search_results.output
        assert len(search_results.items) == 1
        assert search_results.items[0].value.value == a1
        assert search_results.items[0].value.query == qs3[1]

        index.index.create_snapshot().wait()

        a3 = "Susan can run very fast."
        a4 = "Brenda can fight alligators."
        _ = index.index.insert_many([a3, a4])
        index.index.embed().wait()

        qs4 = ["What can Brenda do?", "What can Ronaldo do?", "What can Jerry do?"]
        search_results = index.index.search(qs4)
        search_results.wait()
        search_results = search_results.output
        assert len(search_results.items) == 1
        assert search_results.items[0].value.value == a4
        assert search_results.items[0].value.query == qs4[0]

        qs4 = [
            "What can Brenda do?",
            "Who should run a marathon?",
            "What can Jerry do?",
        ]
        search_results = index.index.search(qs4, k=2)
        search_results.wait()
        search_results = search_results.output
        assert len(search_results.items) == 2
        assert search_results.items[0].value.value == a4
        assert search_results.items[0].value.query == qs4[0]
        assert search_results.items[1].value.value == a3
        assert search_results.items[1].value.query == qs4[1]


def test_empty_queries():
    steamship = get_steamship_client()
    with random_index(steamship, _TEST_EMBEDDER) as index:
        a1 = "Ted can eat an entire block of cheese."
        a2 = "Joe can drink an entire glass of water."
        _ = index.index.insert_many([a1, a2])
        index.index.embed().wait()

        with pytest.raises(SteamshipError):
            _ = index.index.search(None)

        # These technically don't count as empty. Leaving this test in here
        # to encode and capture that in case we want to change it.
        search_results = index.index.search([])
        search_results.wait()
        search_results = search_results.output
        # noinspection PyUnresolvedReferences
        assert len(search_results.items) == 0

        search_results = index.index.search("")
        search_results.wait()
        search_results = search_results.output
        # noinspection PyUnresolvedReferences
        assert len(search_results.items) == 1
