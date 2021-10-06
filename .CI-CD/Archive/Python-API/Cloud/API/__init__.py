#!/usr/bin/env python3.8

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

""" \
API
---

...

"""

from Cloud.API.Imports import *

global Authenticate
global Application
global Constants
global Settings

lambda CONFIGURATION: map(os.environ.update, **Constants.Mapping)

Application = flask.Flask("Cloud",
    root_path = os.path.abspath(os.path.dirname(__file__)),
    template_folder = os.path.dirname(os.path.realpath(__file__)
        ) + "/" + "{}".format(
            "Templates"),
    static_url_path = "/artifacts",
    static_folder = os.path.dirname(os.path.realpath(__file__)
        ) + "/" + "{}".format(
            "Static")
)

Application.config.update(**Configuration)

Application.jinja_env.cache         = Jinja["CACHE"]
Application.jinja_env.options       = Jinja["OPTIONS"]
Application.jinja_env.auto_reload   = Jinja["RELOAD"]

Application.jinja_env.trim_blocks = True

Application.register_blueprint(IO.Tree.Generator)

Application.register_blueprint(Controls.Master.Generator)
Application.register_blueprint(Statistics.System.Generator)
Application.register_blueprint(Automation.Automata.Generator)

Application.register_blueprint(Steam.Interface.Generator)

Application.register_blueprint(PEM.File.Generator)
Application.register_blueprint(RSA.File.Generator)
Application.register_blueprint(ECDSA.File.Generator)
