#!/usr/bin/env python

import os
from setuptools import find_packages, setup
from io import open


with open("README.rst") as readme_file:
    README = readme_file.read()


NAME            = "zai"
VERSION         = "0.0.1"
AUTHOR          = "Zalando SE"
AUTHOR_EMAIL    = "elgalu3@gmail.com"
DESCRIPTION     = "Zalando Data Lake client library helpers and CLI"
LICENSE         = "MIT license"
KEYWORDS        = "zai, zalando, ai"
URL             = "https://github.com/zdatalake/zai"

PACKAGES        = find_packages( where="zai" )
CLASSIFIERS     = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
]
INSTALL_REQUIRES    = [

]
ENTRY_POINTS        = {}
EXTRA_REQUIRES      = {
    "dev"   : [ "sphinx" ],
    "test"  : [ "pytest" ]
}
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
    extra_requires          = EXTRA_REQUIRES,
    entry_points            = ENTRY_POINTS,
    license                 = LICENSE,
    project_urls            = PROJECT_URLS,
)
