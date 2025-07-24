from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="laughbit",
    version="0.1.2",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "requests",
        "typer",
        "rich",
        "typing_extensions"
    ],
    entry_points={
        "console_scripts": [
            "laughbit=laughbit.main:app",
        ],
    },
)
