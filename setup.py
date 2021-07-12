from setuptools import find_packages, setup

setup(
    name="thedaily",
    packages=find_packages(exclude=["tests", "tests."])
)
