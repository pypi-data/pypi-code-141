from setuptools import setup, find_packages
from os import path

# To use a consistent encoding
from codecs import open

HERE = path.abspath(path.dirname(__file__))

# trick to manage package versions in one place only
# http://stackoverflow.com/questions/458550/standard-way-to-embed-version-into-python-package
import re

VERSIONFILE = "lookmlhelper/VERSION.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    VERSIONSTRING = mo.group(1)
else:
    raise RuntimeError(
        "Unable to find version string in %s." % (VERSIONFILE, ))

# Get the long description from the README file
with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Parse requirements.txt file so to have one single source of truth
REQUIREMENTS_DATA = []
with open(path.join(HERE, "requirements.txt"), encoding="utf-8") as f:
    for l in f.readlines():
        if not l.startswith("#"):
            if ">=" in l:
                REQUIREMENTS_DATA.append([l.split(">=")[0]])
            elif "=" in l:
                REQUIREMENTS_DATA.append([l.split("=")[0]])

setup(
    name="lookml-helper",
    version=VERSIONSTRING,
    description="Package to generate LookML from GBQ databases.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/digital-science/dimensions/data-solutions/looker-lookml-generator",
    packages=find_packages(),
    include_package_data=True,
    install_requires=REQUIREMENTS_DATA,
    entry_points='''
        [console_scripts]
        lookml-helper = lookmlhelper.main_cli:main_cli
        quicktest_lookmlhelper = lookmlhelper.tests.quicktest:quicktest_cli
    ''',
)



