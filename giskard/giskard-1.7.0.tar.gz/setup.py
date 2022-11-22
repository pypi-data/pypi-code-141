# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['giskard',
 'giskard.client',
 'giskard.ml_worker',
 'giskard.ml_worker.bridge',
 'giskard.ml_worker.core',
 'giskard.ml_worker.exceptions',
 'giskard.ml_worker.generated',
 'giskard.ml_worker.server',
 'giskard.ml_worker.testing',
 'giskard.ml_worker.utils']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.11.1,<5.0.0',
 'click>=8.1.3,<9.0.0',
 'cloudpickle>=2.1.0,<3.0.0',
 'eli5>=0.13.0,<0.14.0',
 'grpcio-status>=1.46.3,<2.0.0',
 'grpcio>=1.46.3,<2.0.0',
 'importlib_metadata>=4.11.4,<5.0.0',
 'ipython>=7.0.0,<8.0.0',
 'lockfile>=0.12.2,<0.13.0',
 'mixpanel>=4.10.0,<5.0.0',
 'numpy>=1.21.6,<1.22.0',
 'pandas>=1.3.5,<2.0.0',
 'protobuf>=3.9.2,<4.0.0',
 'psutil>=5.9.2,<6.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'python-daemon>=2.3.1,<3.0.0',
 'requests-toolbelt>=0.9.1,<0.10.0',
 'requests>=2.28.1,<3.0.0',
 'scikit-learn>=1.0.0,<1.1.0',
 'scipy>=1.7.2,<1.8',
 'setuptools>=65.4.1,<66.0.0',
 'shap>=0.41.0,<0.42.0',
 'tenacity>=8.1.0,<9.0.0',
 'tqdm>=4.64.1,<5.0.0',
 'zstandard>=0.15.2,<0.16.0']

entry_points = \
{'console_scripts': ['giskard = giskard.cli:cli']}

setup_kwargs = {
    'name': 'giskard',
    'version': '1.7.0',
    'description': 'Inspect your AI models visually, find bugs, give feedback 🕵️\u200d♀️ 💬',
    'long_description': '# Giskard Client\n\n<div align="center">\n\n[![Python Version](https://img.shields.io/pypi/pyversions/giskard-client.svg)](https://pypi.org/project/giskard-client/)\n[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/Giskard-AI/giskard-client/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)\n[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/Giskard-AI/giskard-client/blob/main/.pre-commit-config.yaml)\n[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/Giskard-AI/giskard-client/releases)\n[![License](https://img.shields.io/github/license/Giskard-AI/giskard-client)](https://github.com/Giskard-AI/giskard-client/blob/main/LICENSE)\n\nInspect your AI models visually, find bugs, give feedback 🕵️\u200d♀️ 💬\n\n</div>\n\n## Very first steps\n\n### Initial\n1. Clone the project in a local directory\n\n2. Using `pyenv` setup a local python 3.7\n\n3. If you don\'t have `Poetry` installed run:\n\n```bash\nmake download-poetry\n```\n\n4. Initialize poetry and install `pre-commit` hooks:\n\n```bash\nmake install\n```\n\n5. Tests folder contain scripts that can upload data to your Giskard Backend. Run them using\n```bash \nmake test\n```\nOr individually:\n\n```bash \npoetry run pytest tests/model_inspector/test_upload_text_classification.py\n```\n\nMake sure you have setup the correct URL, as well as your Giskard API token in a `.env` file at the root of the project. \n\n### Poetry\n\nWant to know more about Poetry? Check [its documentation](https://python-poetry.org/docs/).\n\n<details>\n<summary>Details about Poetry</summary>\n<p>\n\nPoetry\'s [commands](https://python-poetry.org/docs/cli/#commands) are very intuitive and easy to learn, like:\n\n- `poetry add numpy@latest`\n- `poetry run pytest`\n- `poetry publish --build`\n\netc\n</p>\n</details>\n\n### Building and releasing your package\n\nBuilding a new version of the application contains steps:\n\n- Bump the version of your package `poetry version <version>`. You can pass the new version explicitly, or a rule such as `major`, `minor`, or `patch`. For more details, refer to the [Semantic Versions](https://semver.org/) standard.\n- Make a commit to `GitHub`.\n- Create a `GitHub release`.\n- And... publish 🙂 `poetry publish --build`\n\n## 🎯 What\'s next\n\nWell, that\'s up to you 💪🏻. I can only recommend the packages and articles that helped me.\n\n- [`Typer`](https://github.com/tiangolo/typer) is great for creating CLI applications.\n- [`Rich`](https://github.com/willmcgugan/rich) makes it easy to add beautiful formatting in the terminal.\n- [`Pydantic`](https://github.com/samuelcolvin/pydantic/) – data validation and settings management using Python type hinting.\n- [`Loguru`](https://github.com/Delgan/loguru) makes logging (stupidly) simple.\n- [`tqdm`](https://github.com/tqdm/tqdm) – fast, extensible progress bar for Python and CLI.\n- [`IceCream`](https://github.com/gruns/icecream) is a little library for sweet and creamy debugging.\n- [`orjson`](https://github.com/ijl/orjson) – ultra fast JSON parsing library.\n- [`Returns`](https://github.com/dry-python/returns) makes you function\'s output meaningful, typed, and safe!\n- [`Hydra`](https://github.com/facebookresearch/hydra) is a framework for elegantly configuring complex applications.\n- [`FastAPI`](https://github.com/tiangolo/fastapi) is a type-driven asynchronous web framework.\n\nArticles:\n\n- [Open Source Guides](https://opensource.guide/).\n- [A handy guide to financial support for open source](https://github.com/nayafia/lemonade-stand)\n- [GitHub Actions Documentation](https://help.github.com/en/actions).\n- Maybe you would like to add [gitmoji](https://gitmoji.carloscuesta.me/) to commit names. This is really funny. 😄\n\n## 🚀 Features\n\n### Development features\n\n- Supports for `Python 3.7` and higher.\n- [`Poetry`](https://python-poetry.org/) as the dependencies manager. See configuration in [`pyproject.toml`](https://github.com/Giskard-AI/giskard-client/blob/main/pyproject.toml) and [`setup.cfg`](https://github.com/Giskard-AI/giskard-client/blob/main/setup.cfg).\n- Automatic codestyle with [`black`](https://github.com/psf/black), [`isort`](https://github.com/timothycrosley/isort) and [`pyupgrade`](https://github.com/asottile/pyupgrade).\n- Ready-to-use [`pre-commit`](https://pre-commit.com/) hooks with code-formatting.\n- Type checks with [`mypy`](https://mypy.readthedocs.io); docstring checks with [`darglint`](https://github.com/terrencepreilly/darglint); security checks with [`safety`](https://github.com/pyupio/safety) and [`bandit`](https://github.com/PyCQA/bandit)\n- Testing with [`pytest`](https://docs.pytest.org/en/latest/).\n- Ready-to-use [`.editorconfig`](https://github.com/Giskard-AI/giskard-client/blob/main/.editorconfig), [`.dockerignore`](https://github.com/Giskard-AI/giskard-client/blob/main/.dockerignore), and [`.gitignore`](https://github.com/Giskard-AI/giskard-client/blob/main/.gitignore). You don\'t have to worry about those things.\n\n### Deployment features\n\n- `GitHub` integration: issue and pr templates.\n- `Github Actions` with predefined [build workflow](https://github.com/Giskard-AI/giskard-client/blob/main/.github/workflows/build.yml) as the default CI/CD.\n- Everything is already set up for security checks, codestyle checks, code formatting, testing, linting, docker builds, etc with [`Makefile`](https://github.com/Giskard-AI/giskard-client/blob/main/Makefile#L89). More details in [makefile-usage](#makefile-usage).\n- [Dockerfile](https://github.com/Giskard-AI/giskard-client/blob/main/docker/Dockerfile) for your package.\n- Always up-to-date dependencies with [`@dependabot`](https://dependabot.com/). You will only [enable it](https://docs.github.com/en/github/administering-a-repository/enabling-and-disabling-version-updates#enabling-github-dependabot-version-updates).\n- Automatic drafts of new releases with [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). You may see the list of labels in [`release-drafter.yml`](https://github.com/Giskard-AI/giskard-client/blob/main/.github/release-drafter.yml). Works perfectly with [Semantic Versions](https://semver.org/) specification.\n\n### Open source community features\n\n- Ready-to-use [Pull Requests templates](https://github.com/Giskard-AI/giskard-client/blob/main/.github/PULL_REQUEST_TEMPLATE.md) and several [Issue templates](https://github.com/Giskard-AI/giskard-client/tree/main/.github/ISSUE_TEMPLATE).\n- Files such as: `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` are generated automatically.\n- [`Stale bot`](https://github.com/apps/stale) that closes abandoned issues after a period of inactivity. (You will only [need to setup free plan](https://github.com/marketplace/stale)). Configuration is [here](https://github.com/Giskard-AI/giskard-client/blob/main/.github/.stale.yml).\n- [Semantic Versions](https://semver.org/) specification with [`Release Drafter`](https://github.com/marketplace/actions/release-drafter).\n\n## Installation\n\n```bash\npip install -U giskard-client\n```\n\nor install with `Poetry`\n\n```bash\npoetry add giskard-client\n```\n\n\n\n### Makefile usage\n\n[`Makefile`](https://github.com/Giskard-AI/giskard-client/blob/main/Makefile) contains a lot of functions for faster development.\n\n<details>\n<summary>1. Download and remove Poetry</summary>\n<p>\n\nTo download and install Poetry run:\n\n```bash\nmake poetry-download\n```\n\nTo uninstall\n\n```bash\nmake poetry-remove\n```\n\n</p>\n</details>\n\n<details>\n<summary>2. Install all dependencies and pre-commit hooks</summary>\n<p>\n\nInstall requirements:\n\n```bash\nmake install\n```\n\nPre-commit hooks coulb be installed after `git init` via\n\n```bash\nmake pre-commit-install\n```\n\n</p>\n</details>\n\n<details>\n<summary>3. Codestyle</summary>\n<p>\n\nAutomatic formatting uses `pyupgrade`, `isort` and `black`.\n\n```bash\nmake codestyle\n\n# or use synonym\nmake formatting\n```\n\nCodestyle checks only, without rewriting files:\n\n```bash\nmake check-codestyle\n```\n\n> Note: `check-codestyle` uses `isort`, `black` and `darglint` library\n\n<details>\n<summary>4. Code security</summary>\n<p>\n\n```bash\nmake check-safety\n```\n\nThis command launches `Poetry` integrity checks as well as identifies security issues with `Safety` and `Bandit`.\n\n```bash\nmake check-safety\n```\n\n</p>\n</details>\n\n</p>\n</details>\n\n<details>\n<summary>5. Type checks</summary>\n<p>\n\nRun `mypy` static type checker\n\n```bash\nmake mypy\n```\n\n</p>\n</details>\n\n<details>\n<summary>6. Tests</summary>\n<p>\n\nRun `pytest`\n\n```bash\nmake test\n```\n\n</p>\n</details>\n\n<details>\n<summary>7. All linters</summary>\n<p>\n\nOf course there is a command to ~~rule~~ run all linters in one:\n\n```bash\nmake lint\n```\n\nthe same as:\n\n```bash\nmake test && make check-codestyle && make mypy && make check-safety\n```\n\n</p>\n</details>\n\n<details>\n<summary>8. Docker</summary>\n<p>\n\n```bash\nmake docker-build\n```\n\nwhich is equivalent to:\n\n```bash\nmake docker-build VERSION=latest\n```\n\nRemove docker image with\n\n```bash\nmake docker-remove\n```\n\nMore information [about docker](https://github.com/Giskard-AI/giskard-client/tree/main/docker).\n\n</p>\n</details>\n\n<details>\n<summary>9. Cleanup</summary>\n<p>\nDelete pycache files\n\n```bash\nmake pycache-remove\n```\n\nRemove package build\n\n```bash\nmake build-remove\n```\n\nOr to remove pycache, build and docker image run:\n\n```bash\nmake clean-all\n```\n\n</p>\n</details>\n\n## 📈 Releases\n\nYou can see the list of available releases on the [GitHub Releases](https://github.com/Giskard-AI/giskard-client/releases) page.\n\nWe follow [Semantic Versions](https://semver.org/) specification.\n\nWe use [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.\n\n### List of labels and corresponding titles\n\n|               **Label**               |  **Title in Releases**  |\n| :-----------------------------------: | :---------------------: |\n|       `enhancement`, `feature`        |       🚀 Features       |\n| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |\n|       `build`, `ci`, `testing`        | 📦 Build System & CI/CD |\n|              `breaking`               |   💥 Breaking Changes   |\n|            `documentation`            |    📝 Documentation     |\n|            `dependencies`             | ⬆️ Dependencies updates |\n\nYou can update it in [`release-drafter.yml`](https://github.com/Giskard-AI/giskard-client/blob/main/.github/release-drafter.yml).\n\nGitHub creates the `bug`, `enhancement`, and `documentation` labels for you. Dependabot creates the `dependencies` label. Create the remaining labels on the Issues tab of your GitHub repository, when you need them.\n\n## 🛡 License\n\n[![License](https://img.shields.io/github/license/Giskard-AI/giskard-client)](https://github.com/Giskard-AI/giskard-client/blob/main/LICENSE)\n\nThis project is licensed under the terms of the `Apache Software License 2.0` license. See [LICENSE](https://github.com/Giskard-AI/giskard-client/blob/main/LICENSE) for more details.\n\n## 📃 Citation\n\n```bibtex\n@misc{giskard-client,\n  author = {Giskard AI},\n  title = {Inspect your AI models visually, find bugs, give feedback 🕵️\u200d♀️ 💬},\n  year = {2021},\n  publisher = {GitHub},\n  journal = {GitHub repository},\n  howpublished = {\\url{https://github.com/Giskard-AI/giskard-client\n}\n```\n\n## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)\n\nThis project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)\n',
    'author': 'Giskard AI',
    'author_email': 'hello@giskard.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Giskard-AI/giskard-client',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.5,<3.11',
}


setup(**setup_kwargs)
