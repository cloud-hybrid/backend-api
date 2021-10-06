#!/usr/bin/env python3

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:   *.*  -*- #

# Owner: Jacob B. Sanders
# Source: code.cloud-technology.io
# License: BSD 3-Clause License

# Copyright 2020, Jacob B. Sanders

#
# ========================================================================
# Axon Setup.PY
# ========================================================================
#
# Notes
# -----
# - Version Format: major.minor[.patch[.sub]]
#   - https://docs.python.org/3/distutils/setupscript.html#additional-meta-data

import os
import sys
import shlex

import subprocess

import setuptools

GIT_API_ENDPOINT = ""

os.environ["DISTUTILS_DEBUG"] = "True"

Installer   = setuptools.setup
Packages    = setuptools.find_packages

URLs        = {
    "Documentation": "https://packaging.python.org/tutorials/distributing-packages/",
    "Funding": "https://donate.pypi.org",
    "Say Thanks!": "http://saythanks.io/to/example",
    "Source": "https://github.com/pypa/sampleproject/",
    "Tracker": "https://github.com/pypa/sampleproject/issues",
}

Requirements = [
    "flask",
    "psutil",
    "wheel",
    "uwsgi",
    "urllib3",
    "sphinx",
    "PyYAML",
    "boto3",
    "setuptools",
    "awscli",
    "sphinx_theme",
    "crypto",
    "werkzeug"
]

Dependencies = [
    "flask",
    "psutil",
    "wheel",
    "uwsgi",
    "urllib3",
    "sphinx",
    "awscli",
    "boto3",
    "setuptools",
    "PyYAML",
    "sphinx_theme",
    "crypto",
    "werkzeug",
    "Jinja2"
]

Classifiers = [
    "Programming Language :: Python :: 3",
    "License :: Private :: Authorized Usage Only",
    "Operating System :: OS Independent",
],

Files = [
    "Cloud/API/Database/Cloud-Hybrid.db",
    "Cloud/API/DB/Cloud-API.db"
]

setuptools.setup(
    name = "Cloud",
    version = "1.0.0",
    author = "Jacob B. Sanders",
    author_email = "jacob.sanders@cloudhybrid.io",
    description = "",
    project_urls = URLs,
    long_description = "",
    long_description_content_type = "text/markdown",
    url = "https://gitlab.cloudhybrid.io/IaC/Cloud-API",
    packages = Packages(),
    classifiers = Classifiers,
    data_files = Files,
    python_requires = ">=3.8",
    include_package_data = True,
    requires =  Requirements,
    install_requires = Dependencies,
    entry_points = {
        "console_scripts": [
            "Cloud=Cloud.WSGI:main"
        ]
    }
)

Source = "{}/.../Distribution/{}".format(
        os.path.abspath(os.path.dirname(__file__)),
            "Cloud-1.0.0-1-Development-Build-Python-3.8-none-Linux.whl"
)

if os.path.isfile(Source):
    Target = Source.replace("-none", "")
    process = subprocess.Popen(
        shlex.split(
            "{}".format("mv %s %s" % (Source, Target))
        ),
        shell = False,
        stdout = sys.__stdout__,
        stderr = subprocess.PIPE,
        stdin = subprocess.DEVNULL,
        encoding = "UTF-8"
    ); process.wait(timeout = 30)

    if Error := process.communicate()[-1]: sys.stdout.write(Error + "\n")
