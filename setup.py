from pathlib import Path

from setuptools import find_packages, setup


def read_requirements():
    try:
        return list(Path("requirements.txt").read_text().splitlines())[1:]
    except FileNotFoundError:
        return []


setup(
    name="bard-cli",
    version="0.1.0",
    description="A CLI for the Bard API",
    maintainer="Rohan Yadav",
    maintainer_email="rohanya.76426@gmail.com",
    packages=find_packages(),
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "bard-cli = bard-cli.main:main",
        ],
    },
)
