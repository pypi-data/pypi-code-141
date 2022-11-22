from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="multi-search",
    version="0.0.1",
    author="tyler jones",
    description="Simple ui wrapper and utility for single script search tools in python.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/tylerhjones/multi-search/",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        "console_scripts": [
            "ms = app:main",
        ],
    },
)