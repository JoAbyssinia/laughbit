from setuptools import setup, find_packages

setup(
    name="laughbit",
    version="0.1.0",
    packages=find_packages(),
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
