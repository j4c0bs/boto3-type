# -*- coding: utf-8 -*-


import codecs
import os.path
import re

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))


with open("README.md", "r") as fh:
    long_description = fh.read()


def read(*parts):
    with codecs.open(os.path.join(here, *parts), "r") as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="boto3_type",
    version=find_version("boto3_type", "__init__.py"),
    author="Jeremy Jacobs",
    author_email="pub@j4c0bs.net",
    description="Boto3 service type check",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3",
    packages=find_packages(exclude=["docs*", "tests*"]),
    include_package_data=False,
    install_requires=["boto3", "botocore"],
    license="BSD-2-Clause",
    keywords="aws boto3 botocore",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    project_urls={
        "Source": "https://github.com/j4c0bs/boto3-type",
        "Bug Reports": "https://github.com/j4c0bs/boto3-type/issues",
    },
    url="https://github.com/j4c0bs/boto3-type",
)
