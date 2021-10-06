#!/usr/bin/env file .

# -*-  Coding: UTF-8  -*- #
# -*-  System: Linux  -*- #
# -*-  Usage:  *.Yaml -*- #

# Owner: Jacob B. Sanders
# Source: code.cloud-technology.io
# License: BSD 3-Clause License

#
# Copyright 2020 Jacob B. Sanders - Cloud Hybrid LLC. & Affiliates
#
# Redistribution and use in source and binary forms, with or without modification, are permitted
# provided that the following conditions are met:
#
# 1.  Redistributions of source code must retain the above copyright notice, this list of
#     conditions and the following disclaimer.
#
# 2.  Redistributions in binary form must reproduce the above copyright notice, this list of
#     conditions and the following disclaimer in the documentation and/or other materials
#     provided with the distribution.
#
# 3.  Neither the name of the copyright holder nor the names of its contributors may be used
#     to endorse or promote products derived from this software without specific prior written
#     permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
# OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER
# OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
# OF SUCH DAMAGE.
#

""" STDOUT Module
==================

Python (by default) will buffer writes to STDOUT during run-time;
therefore, in select cases, causing output to printed *after
execution.

File buffering of STDOUT can easily be prevented *before run-time
using "python -u" (or #!/usr/bin/env python -u etc) or by setting
the environment variable `PYTHONUNBUFFERED`.

The sys.stdout can also be replaced with some other stream - such
as a wrapper which does a flush after every call.

Or something similar to the following *may as a run-time solution
in *most use cases::

    >>> #!/usr/bin/env python3
    ...
    >>> \"\"\"
    >>> The `Stream` object will effectively *replace the `sys.stdout`
    >>> object. Additionally, `Stream` will *flush after every write
    >>> made to the Python process'(es) STDOUT while leaving other
    >>> external writes to be buffered.
    >>> \"\"\"
    ...
    >>> import sys
    ...
    >>> class Stream(object):
    ...     def __init__(self, buffer: sys.stdout):
    ...         self.buffer = buffer
    
    ...     def write(self, _IO):
    ...         self.buffer.write(_IO)
    ...         self.buffer.flush()
    
    ...     def __getattr__(self, attr):
    ...         return getattr(self.buffer, attr)
    ...
    >>> sys.stdout = Unbuffered(sys.stdout)
    ...
    >>> print("Hello World")

    'Hello World'

"""

import sys
import typing
import functools

Optional = typing.Optional

Print = functools.partial(print, flush = True)

class Stream(object):
    """ `sys.stdout` File-Buffer Handler

    >>> Stream.disableBuffer()

    The `Stream` object will effectively *replace the `sys.stdout`
    object. Additionally, `Stream` will *flush after every write
    made to the Python process'(es) STDOUT while leaving other
    external writes to be buffered.
    """

    def __init__(self, buffer: sys.stdout):
        self.buffer = buffer

    def write(self, _IO):
        self.buffer.write(_IO)
        self.buffer.flush()

    def __getattr__(self, attr):
        return getattr(self.buffer, attr)

    @classmethod
    def print(cls, *argv: Optional[str|bool], **kwargs: Optional[{}]):
        """ `print()` Built-In Replacement

        Parameters:
            **kwargs (object):
            *argv: (object):

        Keyword Arguments:
            sep:    (Optional[str]):    Argument Separator
            end:    (Optional[str]):    End-Line Character(s)
            file:   (Optional[str]):    Buffered File Descriptor
            flush:  (bool):             Default := `True`

        """

        Print(*argv, **kwargs)

    @staticmethod
    def disableBuffer():
        sys.stdout = Stream(sys.stdout)

__all__ = [ "Stream", "Print", "Optional" ]
