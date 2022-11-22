from setuptools import setup

with open("README.md", "r") as f:

    long_description = f.read()

setup(
    name="hexacolors",
    version="0.4.6",
    url = 'https://github.com/Marciel404/hexacolors',
    author="Marciel404",
    description='''
:A simple library that converts string to hexadecimal understandable by python
:A simple library that converts RGB to hexadecimal understandable by python
:A simple library that converts CMYK to hexadecimal understandable by python
:A simple library that converts HSL to hexadecimal understandable by python
:A simple library that converts hexadecimal understandable by python
''',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["hexacolors","hexacolors.colors"],
    license = 'MIT',
    keywords = 'String hexadecimal converter' ,
    CLASSIFIERS = [
    'Intended Audience :: Developers',
    'Topic :: colors',
    'License :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    ],
    python_requires='>=3.8',
    install_requires=['requests>=2.28.1'],
    dependency_links=['https://github.com/Marciel404/hexacolors']
)