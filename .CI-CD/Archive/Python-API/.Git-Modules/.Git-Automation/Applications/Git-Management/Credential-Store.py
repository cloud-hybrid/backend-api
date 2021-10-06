#!/usr/bin/env python3

# -*-  Coding: UTF-8  -*- #
# -*-  System: Linux  -*- #
# -*-  Usage:  *.PY   -*- #

# @Task: Add Copyright Headers
# @Task: Add Error Docstring

import os
import sys
import shlex
import textwrap
import subprocess
import typing

Format = textwrap.dedent

Object = typing.NamedTuple

class Error(Object):
    """
    
    """
    Username:   RuntimeError = RuntimeError(    "Username Required as Input"    ); \
        setattr(Username,       Default =       "Username Required as Input")
    
    Email:      RuntimeError = RuntimeError(    "Email Required as Input"       ); \
        setattr(Email,          Default =       "Email Required as Input")
    
    Token:      RuntimeError = RuntimeError(    "Token Required as Input"       ); \
        setattr(Token,          Default =       "Token Required as Input")
    
    Authority:  RuntimeError = RuntimeError(    "Authority Required as Input"   ); \
        setattr(Authority,      Default =       "Authority Required as Input")

    def __init__(self, _username: str = "", _email: str = "", _token: str = "", _authority: str = "") -> exit:
        super(self, Error).__init__(self, [
            "_username",
            "_email",
            "_token",
            "_authority"
        ])
        
        self.Username = RuntimeError(
            Error.Username.Default + _username \
            if _username != "" else \
                "Username Required as Input")
        self.Email = RuntimeError(
            Error.Email.Default + _email \
            if _email != "" else \
                "Email Required as Input")
        self.Token = RuntimeError(
            Error.Email.Default + _email \
            if _email != "" else \
                "Token Required as Input")
        self.Authority = RuntimeError(
            Error.Token.Default + _token \
            if _token != "" else \
                "Authority Required as Input")
    
    @classmethod
    def Generate(cls, dot_product: str):
        print(eval("cls.__init__().{}".format(
            dot_product
        ))); exit(255)

class Git(object):
    def __init__(self, git_username: str, git_email: str, git_authority: str, git_password: str = "", *argv, **kwargs):
        self.Directory = os.path.expanduser("~")
        self.User = self.Directory.replace("/hom e/", "").replace("/opt/", "").replace("/usr/", "")
        
        self.Username = git_username
        self.Email = git_email
        self.Password = git_password
        self.FQDN = git_authority
        
    def run(self):
        subprocess.run(
            shlex.split('''bash -c "echo 'https://{0}:{1}@{2}' > {3}/.git-credentials" '''.format(
                self.GitUsername,
                self.Password,
                self.FQDN,
                self.Directory
            )),
            stdout = subprocess.DEVNULL,
            stderr = subprocess.DEVNULL,
            stdin = subprocess.DEVNULL,
            capture_output = False,
            shell = False)

        subprocess.run(
            shlex.split('''bash -c "chown {User} {Directory}/.git-credentials" '''.format(
                User = self.User,
                Directory = self.Directory
            )),
            stdout = subprocess.DEVNULL,
            stderr = subprocess.DEVNULL,
            stdin = subprocess.DEVNULL,
            capture_output = False,
            shell = False)

        with open ("{0}/.gitconfig".format(self.Directory), "w+") as File:
            File.write(Format("""\
                [core]
                        filemode = true

                [user]
                        name = {0}
                        email = {1}

                [credential]
                        helper = store

            """.format(
                self.Username,
                self.Email
            )))

        subprocess.run(
            shlex.split('''bash -c "chown {User} {Directory}/.gitconfig" '''.format(
                User = self.User,
                Directory = self.Directory
            )),
            stdout = subprocess.DEVNULL,
            stderr = subprocess.DEVNULL,
            stdin = subprocess.DEVNULL,
            capture_output = False,
            shell = False)

    @property
    def Error(self) -> Error:
        return Error()
    
def main(*argv):
    print("Validating Input")
    
    git_username:   str = argv[1] if argv[1] else Error.Generate("Username")
    git_email:      str = argv[2] if argv[2] else Error.Generate("Email")
    git_authority:  str = argv[3] if argv[3] else Error.Generate("Authority")
    
    Configurator = Git("Segmentational", "jacob.sanders@cloudhybrid.io", "code.cloud-technology.io")
    
    print("Creating Configuration File(s)")

    Configurator.run()
    
    print("Successful")

if __name__ == "__main__":
    if sys.version_info[0] != 3:
        raise OSError("Error: Python 3 Required")
        sys.exit(-1)
    elif sys.version_info[1] < 8:
        raise OSError("Error: A minimum version of Python 3.8 Required")
        sys.exit(-1)
    else:
        main(*sys.argv)
    
    exit(0)

