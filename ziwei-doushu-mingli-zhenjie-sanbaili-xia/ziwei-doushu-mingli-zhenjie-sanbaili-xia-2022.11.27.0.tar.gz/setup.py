#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import ZiweiDoushuMingliZhenjieSanbailiXia
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('ZiweiDoushuMingliZhenjieSanbailiXia'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="ziwei-doushu-mingli-zhenjie-sanbaili-xia",
    version=ZiweiDoushuMingliZhenjieSanbailiXia.__version__,
    url="https://github.com/apachecn/ziwei-doushu-mingli-zhenjie-sanbaili-xia",
    author=ZiweiDoushuMingliZhenjieSanbailiXia.__author__,
    author_email=ZiweiDoushuMingliZhenjieSanbailiXia.__email__,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: Other/Proprietary License",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Text Processing :: Markup :: Markdown",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Documentation",
        "Topic :: Documentation",
    ],
    description="紫微斗数命例真解三百例下",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "ziwei-doushu-mingli-zhenjie-sanbaili-xia=ZiweiDoushuMingliZhenjieSanbailiXia.__main__:main",
            "ZiweiDoushuMingliZhenjieSanbailiXia=ZiweiDoushuMingliZhenjieSanbailiXia.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
