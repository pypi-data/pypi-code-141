import regex as re
from contextlib import suppress
from typing import Generator

TEMPLATE_NAMES_PATTERN = re.compile("\\{([\\w\\?;][-\\w\\.,]*)\\}")


def tvars(route: str, url: str) -> dict[str, str]:
    """
    Get the variables from a URL given the route template. If the URL does not match the given route, then return {}.

    :param route: the route template.
    :param url: the url that may be a valid one for the given route.
    :return: a dictionary containing references to all the variables from the route that were given in curly braces.
    """
    pattern = _to_regex(route)
    match = pattern.fullmatch(url, partial=True)
    while match and match.partial:
        route = route[:-1]
        with suppress(Exception):
            match = _to_regex(route).fullmatch(url, partial=True)
    return match.groupdict() if match else {}


def _to_regex(route: str) -> re.Pattern:
    """
    Convert a route to a regex pattern.

    For each variable in the route, a capture group is added. Everything else is an exact match.

    :param route: the route template.
    :return: the generated regex pattern.
    """
    metadata_ = _metadata(route)
    l = []
    for m in metadata_:
        if m[3]:
            l.append(r'(?P<' + m[0] + r'>.+)')
        else:
            l.append(m[0])
    return re.compile(''.join(l))


def _metadata(route: str) -> Generator[tuple[str, int, int, bool], None, None]:
    """
    Splits the route into components such that the variables and constants are separate. The function returns a
    generator that yields each component one by one.

    The first index of the yielded content is the content itself. The second and third represents the start and end
    of a range that indicates the indices of the content. The fourth index is a boolean that is True if the content
    is a variable.

    :param route: the route template.
    :return: a 4-tuple containing the content, the start index, the end index (exclusive), and whether it is a
    variable.
    """
    if route is None:
        raise ValueError('route cannot be None')
    m = {match.group(): (match.start(), match.end()) for match in
         TEMPLATE_NAMES_PATTERN.finditer(route)}
    split_ = TEMPLATE_NAMES_PATTERN.split(route)
    start = 0
    i = 0
    for k, v in m.items():
        if v[0] > start:
            yield split_[i], start, v[0], False
            start = v[1]
            i += 1
        yield split_[i], v[0], v[1], True
        i += 1
    else:
        route_len = len(route)
        if route_len > start:
            yield split_[i], start, route_len, False
