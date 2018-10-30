#!/usr/bin/env python
# flake8: noqa
from __future__ import print_function
from setuptools import find_packages, setup
from io import open

import os
import sys
import inspect


if sys.version_info < (3, 0):
  print('zai requires python3.', file=sys.stderr)
  sys.exit(1)

cwd = inspect.getfile(inspect.currentframe())
__location__ = os.path.join(os.getcwd(), os.path.dirname(cwd))


with open("README.rst") as readme_file:
    README = readme_file.read()


def get_install_requirements(path):
    content = open(os.path.join(__location__, path)).read()
    return [req for req in content.split("\\n") if req != ""]


URL             = "https://github.com/zdatalake/zai"
NAME            = "zai"
AUTHOR          = "Zalando SE"
VERSION         = "0.0.1"
LICENSE         = "MIT license"
KEYWORDS        = "zai, zalando, ai"
DESCRIPTION     = "Zalando Data Lake client library helpers and CLI"
AUTHOR_EMAIL    = "elgalu3@gmail.com"
MAIN_PACKAGE    = "zai"
ENTRY_POINTS    = {}

PACKAGES            = find_packages( where=MAIN_PACKAGE )
INSTALL_REQUIRES    = get_install_requirements("requirements.txt")
SETUP_REQUIRES      = [ "pytest-runner" ]
TEST_REQUIRES       = [
    "tox==3.5.3",
    "pytest==3.9.3"
]

EXTRAS_REQUIRE      = {
    "docs"   : [
        "Sphinx==1.8.1",
    ],
}
COMMAND_OPTIONS = {
    "test": {
        "test_suite": ("setup.py", "tests"),
        "cov": ("setup.py", MAIN_PACKAGE)
    }
}
CLASSIFIERS     = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
]

PROJECT_URLS        = {
    "Bug Reports"   : "https://github.com/zdatalake/zai/issues",
    "Source"        : "https://github.com/zdatalake/zai",
}

setup(
    name                    = NAME,
    version                 = VERSION,
    description             = DESCRIPTION,
    long_description        = README,
    url                     = URL,
    author                  = AUTHOR,
    author_email            = AUTHOR_EMAIL,
    classifiers             = CLASSIFIERS,
    keywords                = KEYWORDS,
    packages                = PACKAGES,
    install_requires        = INSTALL_REQUIRES,
    setup_requires          = SETUP_REQUIRES,
    tests_require            = TEST_REQUIRES,
    extras_require          = EXTRAS_REQUIRE,
    entry_points            = ENTRY_POINTS,
    license                 = LICENSE,
    project_urls            = PROJECT_URLS,
)
