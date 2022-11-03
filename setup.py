"""Python setup.py for website_link package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("website_link", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="website_link",
    version=read("website_link", "VERSION"),
    description="Awesome website_link created by gw1770df",
    url="https://github.com/gw1770df/website_link/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="gw1770df",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["website_link = website_link.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
