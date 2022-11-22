from setuptools import setup, find_packages

REQUIRED_PACKAGES = [
    'viggocore>=1.0.0,<2.0.0',
    'flask-cors'
]

setup(
    name="vclocal",
    version="1.0.0",
    summary='VCLOCAL Module Framework',
    description="VCLOCAL backend Flask REST service",
    packages=find_packages(exclude=["tests"]),
    install_requires=REQUIRED_PACKAGES
)
