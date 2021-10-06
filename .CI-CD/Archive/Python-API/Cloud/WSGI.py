#!/usr/bin/env python3.8

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:  *.py  -*- #

#
# ========================================================================
# WSGI.py - Primary WSGI Web-Server Handler
# ========================================================================
# Direct execution of this script introduces unexpected, inconsistent
# bugs.
# 
# WSGI.py should only be called only one of two ways:
#   1. Indirectly via __init__ & __main__
#   2. Directly via uWSGI or related WSGI-server callable
# 
# Option one should only be used when in development; such is useful when
# debugging or dynamic loading of & updates upon code change. Please refer
# to the docstring listed below for other *primarily* development-based
# callable(s) & methods.
#

"""\
Primary WSGI Web-Server Handler

Direct execution of this script introduces unexpected, inconsistent bugs.

>>> python -m Cloud

>>> uWSGI --yaml WSGI.Yaml

>>> nohup uwsgi \
...     --socket 0.0.0.0:9999 \
...     --wsgi-file WSGI.py \
...     --callable Application \
...         --processes 16 \
...         --threads 8 \
...         --buffer-size 24576 \
...             &

>>> nohup uwsgi --ini WSGI.ini &

>>> sudo bash -c cat << EOF > /etc/systemd/system/api.uwsgi.service
... [Unit]
... Description=Cloud-Hybrid
... After=syslog.target
... 
... [Service]
... ExecStart=/usr/bin/env uwsgi --ini /opt/api/wsgi.ini
... RuntimeDirectory=uwsgi
... Restart=always
... KillSignal=SIGQUIT
... Type=notify
... StandardError=syslog
... NotifyAccess=all
... 
... [Install]
... WantedBy=multi-user.target
... EOF

Please make sure in advance that any `app.run()` calls are inside an
`if __name__ == '__main__':` block or moved to a separate file. The 
`App.run()` line cannot be called because such will always start a local WSGI
server which cannot be used nor acceptable in a production WSGI environment.

>>> systemctl start api.uwsgi.service

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

import Cloud
import Cloud.API
import Cloud.API.Imports

from Cloud.API.Imports import *

Application = Cloud.API.Application

class Handler(object):
    Application = Application

    def __enter__(self):
        return self

    def __exit__(self, type, value, handler):
        SystemExit(type, value, handler)

    def __init__(self, *argv, **kwargs):
        self.run(debug = True)

    def run(self, debug: bool = False):
        try: self.start()
        except KeyboardInterrupt:
            self.__exit__(KeyboardInterrupt(
                "Keyboard-Interrupt",0, None))
        finally:
            exit(0)

    def start(self):
        self.Application.run(host = "0.0.0.0", port = "5000")
