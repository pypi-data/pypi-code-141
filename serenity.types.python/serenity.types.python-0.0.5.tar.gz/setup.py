# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src/python'}

packages = \
['serenity_types',
 'serenity_types.pricing',
 'serenity_types.pricing.derivatives',
 'serenity_types.pricing.derivatives.options',
 'serenity_types.pricing.derivatives.rates',
 'serenity_types.refdata']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.9.1,<2.0.0']

setup_kwargs = {
    'name': 'serenity.types.python',
    'version': '0.0.5',
    'description': 'Python shared types for the Serenity digital asset risk API',
    'long_description': '# serenity.types.python\n\nThis base repository contains shared classes and enumerations common to the Serenity platform and the public SDK.\nIt is not meant to be used or installed on a standalone basis and is intended for use by Serenity clients only.\n',
    'author': 'Cloudwall Support',
    'author_email': 'support@cloudwall.tech',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
