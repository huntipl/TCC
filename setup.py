from setuptools import setup, find_packages

setup(
    name="tcc",
    version="0.0.1",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])
)
