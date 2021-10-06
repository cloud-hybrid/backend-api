#!/usr/bin/env python3.8

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

"""\
PostgreSQL:
    MacOS:
        - Installation Directory: /Library/PostgreSQL/12
        - Server Installation Directory: /Library/PostgreSQL/12
        - Data Directory: /Library/PostgreSQL/12/data
        - Database Port: 6585
        - Database Superuser: postgres
        - Operating System Account: postgres
        - Database Service: postgresql-12
        - Command Line Tools Installation Directory: /Library/PostgreSQL/12
        - pgAdmin4 Installation Directory: /Library/PostgreSQL/12/pgAdmin 4
        - Stack Builder Installation Directory: /Library/PostgreSQL/12


Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

import os
import sys

import Cloud.Constants

sys.pycache_prefix = ".PYC"

Objects = object
Tuple = tuple
Dictionary = dict
Array = list

Constants = Cloud.Constants

class Configuration(object):
    Version = "1.0.0"

    Author = "Jacob B. Sanders"
    Contact = {
        "Name" : "Jacob B. Sanders",
        "Title" : "Owner, Software & Automation Engineer",
        "Email" : "jacob.sanders@cloudhybrid.io",
        "Phone" : "612-256-9826"
    }

    Company = Constants.Company
    Shortname = Constants.Shortname
    Application = Constants.FQDN + " " + "Web-Application"

    Domain = Constants.Domain
    Base = Constants.FQDN
    FQDN = Constants.FQDN
    HTTP = Constants.HTTP
    Port = Constants.Port

    Statics = "artifacts"

    Directories = {
        "Statics"    : "{}/{}".format(Domain, Statics),
        "Images"     : "{}/{}/{}".format(Domain, Statics, "Images"),
        "Favicons"   : "{}/{}/{}".format(Domain, Statics, "Favicon-IO"),
        "Javascript" : "{}/{}/{}".format(Domain, Statics, "Javascript"),
        "Syntax"     : "{}/{}/{}".format(Domain, Statics, "Syntax"),
        "UI"         : "{}/{}/{}".format(Domain, Statics, "User-Interface"),
        "Styles"     : "{}/{}/{}".format(Domain, Statics, "Styles"),
        "Fonts"      : "{}/{}/{}".format(Domain, Statics, "Font-Book"),
        "Documents"  : "{}/{}/{}".format(Domain, Statics, "Documentation")
    }

    Favicons = {
        "General" : {
            "Standard"  : Directories["Favicons"] + "/" + "favicon.ico",
            "Small"     : Directories["Favicons"] + "/" + "favicon-16x16.png",
            "Large"     : Directories["Favicons"] + "/" + "favicon-32x32.png"
        },
        "Android" : {
            "Standard"  : Directories["Favicons"] + "/" + "android-chrome-192x192.png",
            "Large"     : Directories["Favicons"] + "/" + "android-chrome-512x512.png",
        },
        "Apple" : Directories["Favicons"] + "/" + "apple-touch-icon.png"
    }

    AWS = {
        "ID"        : os.getenv("AWS_ACCESS_KEY_ID", Constants.AWS_ACCESS_KEY_ID),
        "Token"     : os.getenv("AWS_SECRET_ACCESS_KEY", Constants.AWS_SECRET_ACCESS_KEY),
        "Region"    : os.getenv("AWS_DEFAULT_REGION", Constants.AWS_DEFAULT_REGION),
        "Output"    : os.getenv("AWS_DEFAULT_OUTPUT", Constants.AWS_DEFAULT_OUTPUT),
        "Console"   : "https://cloudhybrid.signin.aws.amazon.com/console",
        "Account"   : "Cloud-Hybrid"
    }

    Token = Constants.SECRET_KEY
    JWN = Constants.Vault.JWN
    JTI = Constants.Cryptic.JTI()

    os.environ["AWS_ACCESS_KEY_ID"]        = "{}".format(AWS["ID"])
    os.environ["AWS_SECRET_ACCESS_KEY"]    = "{}".format(AWS["Token"])
    os.environ["AWS_DEFAULT_REGION"]       = "{}".format(AWS["Region"])
    os.environ["AWS_DEFAULT_OUTPUT"]       = "{}".format(AWS["Output"])

    PostgreSQL = {
        "Locale" : "en_US.UTF-8",
        "Port" : 6585,
        "Super-User" : "postgres",
        "Password"   : "Kn0wledge!"
    }

    def __init__(self, *argv, **kwargs):
        """ Configurations
        ------------------
        - argv:     Treat unpacked values contained in `argv` as initializer flags.
        - kwargs:   Use Key-Value pairs defined in `kwargs` as additional object
                    attributes & properties.

        """

        lambda FLAG: map(setattr(self, "{}".format(FLAG), True, argv))

        map(setattr, kwargs.items())

    def __getattr__(self, name):
        """ Simple helper method for looking up an instantiated object's dot-product if the
        object was initially given a Key-Dash-Value assignment.

        Called when the default attribute access fails with an AttributeError (either
        __getattribute__() raises an AttributeError because name is not an instance attribute
        or an attribute in the class tree for self; or __get__() of a name property raises
        AttributeError). The `__getattr__` method should either return the (computed) attribute
        value or raise an AttributeError exception.

        """

        source = str(name)
        target = source.replace("-", "_")

        try: return self.target
        except:
            if self.__dict__.get(source, None): return self.__dict__.get(source, None)
            else: raise ValueError("{} Not Found. {}".format(
                source,
                self.__dict__.items()
            ))
