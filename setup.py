#!/usr/bin/python3

# -*- Coding: UTF-8 -*-
# -*- System: Linux -*-
# -*- Usage:   *.*  -*-

import os
import sys
import glob
import time
import json
import shlex
import shutil
import urllib
import typing
import platform
import textwrap
import warnings
import setuptools
import subprocess
import configparser

import urllib.request

warnings.filterwarnings("ignore")

class Meta:
    Copyright = textwrap.dedent("""\
        #!/usr/bin/env python3

        # -*- Coding: UTF-8 -*-
        # -*- System: Linux -*-
        # -*- Usage:   *.*  -*-

        # Creator:  Jacob B. Sanders
        # Location: gitlab.cloud-technology.io
        # License:  BSD 3-Clause License
    """)

CWD = Path = os.path.abspath(os.path.dirname(__file__))

assert os.path.isfile(os.path.join(CWD, "Environment.ini"))

shutil.copy(CWD + os.sep + "Environment.ini", CWD + os.sep + ".CI-CD")

subprocess.run(
    shlex.split("{0} {1} Environment.ini".format(
        sys.executable, os.path.join(CWD, ".CI-CD" + os.sep + "Sanitize.py")
    ))
)

Version = ".".join(open(CWD + os.sep + "VERSION", "r").readline().split())
URL = "https://gitlab.cloud-technology.io/Nexus/API.git"
if sys.argv[-1] == "--Install" or sys.argv[-1] == "--install":
    Install = True
    sys.argv.pop()
else:
    Install = False

sys.stdout.write("[Backend-API]: API CI-CD Build ➜ {0}".format(Version) + "\n")
sys.stdout.flush()

sys.stdout.write("[Backend-API]: Initializing Target(s) ➜ ")
sys.stdout.flush()

Name = "Backend-API"
Debugging = os.environ["DISTUTILS_DEBUG"] = "0"
Distribution = Path + os.sep + "Artifact" + os.sep + "Distribution"
Environment = os.environ.get("VIRTUAL_ENV", False)
System = platform.system() in ["Linux", "Darwin", "Java"]
TTY = os.isatty(sys.stdin.fileno())

sys.stdout.write("Initialized" + "\n")
sys.stdout.flush()

Any = typing.Any
List = typing.List

exit(128) if System == False else ...

if Environment == False and TTY == True:
    if Environment is False and os.path.isdir(os.path.dirname(__file__) + os.sep + ".venv"):
        os.environ["VIRTUAL_ENV"] = os.path.dirname(__file__) + os.sep + ".venv"
        os.system("alias python=python3")
    else:
        sys.stdout.write("Error: Virtual Environment Not Activated" + "\n")
        exit(129)
elif Environment == False and TTY == False:
    sys.stdout.write("Warning: Virtual Environment Not Activated; TTY Unavailable" + "\n")
else:
    os.system("alias python=python3")

sys.stdout.write("[Backend-API]: Writing Configurations ➜ ")
sys.stdout.flush()

Installer = setuptools.setup
Packages = setuptools.find_packages

Configuration = """\
[global]
verbose = 0

[options]
zip_safe = True
include_package_data = True

[build]
build_base    = Artifact/Build
build_purelib = Artifact/Build/Standard
build_scripts = Artifact/Build/Scripting
build_lib     = Artifact/Build/Library

[bdist_rpm]
vendor = Cloud-Technology

[sdist]
dist_dir = Artifact/Distribution/Source

[bdist]
bdist_base  = Artifact/Distribution/Binary
dist_dir    = Artifact/Distribution
formats     = zip

[bdist_egg]
dist_dir                = Artifact/Distribution
keep_temp               = False
bdist_dir               = Artifact/Distribution/Egg
skip_build              = False
exclude_source_files    = True

[bdist_wheel]
bdist_dir       = Artifact/Distribution/Binary
dist_dir        = Artifact/Distribution

[bdist_msi]
vendor      = Cloud-Technology
doc_files   = README.md
""".format(CWD)

CFG = open(CWD + os.sep + "setup.cfg", "w+")
CFG.write(Configuration)
CFG.close()
sys.stdout.write("Wrote" + "\n")
sys.stdout.flush()

sys.stdout.write("[Backend-API]: Updating __version__.py ➜ ")
sys.stdout.flush()

Target = open(CWD + os.sep + "API" + os.sep + "__version__.py", "w+")

Delimited = Version.split(".")
Major, Minor, Patch = Delimited[0], Delimited[1], Delimited[2]

Target.write(Meta.Copyright + "\n"
    + "__version__ = (%s, %s, %s)" % (Major, Minor, Patch)
    + "\n"
); Target.close()

sys.stdout.write("Updated" + "\n")

sys.stdout.write("[Backend-API]: Generating TLS Certificate ➜ ")
sys.stdout.flush()

Subject = "/C=US/ST=MN/O=Cloud Technology LLC./CN=backend.cloud-technology.io/subjectAltName=DNS:*.backend.cloud-technology.io,DNS:backend.cloud-technology.io,Development,0.0.0.0"

denormalized = """\
openssl req -x509 -newkey rsa:8192 -nodes \
    -sha256 -subj "{0}"                   \
        -keyout "{1}/.CI-CD/Key.PEM" -out        \
           {1}/.CI-CD/Key.PEM
""".format(Subject, CWD)

command = shlex.split(denormalized)
TLS = subprocess.Popen(
    args = command,
    shell = False,
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)

try:
    Response = TLS.communicate(timeout = 60)

    TLS.poll()

    sys.stdout.write("Key.PEM - 8192 Bytes" + "\n")
    sys.stdout.flush()

except subprocess.TimeoutExpired as Error:
    sys.stdout.write("[WARNING] - Open-SSL TLS Certificate Was Not Generated." + "\n")
    sys.stdout.write("    Please Install OpenSSL if Applicable. A Development PEM" + "\n")
    sys.stdout.write("    will be Issued as a Temporary Solution " + "\n")
    sys.stdout.flush()

sys.stdout.write("[Backend-API]: Copying Data to Target(s) ➜ ")
sys.stdout.flush()

shutil.copy("VERSION", CWD + os.sep + "Server/VERSION")
File = open(CWD + os.sep + "API" + os.sep + "Version.py", "w+")
Content = "Value = \"{0}\"".format(open(CWD + os.sep + "VERSION", "r").readline().strip())
File.write(Content)
File.close()

if os.path.isfile(CWD + os.sep + "Development.key"):
    shutil.copy(CWD + os.sep + "Development.key", CWD + os.sep + "Server/Development.key")
    shutil.copy(CWD + os.sep + "Development.crt", CWD + os.sep + "Server/Development.crt")
    shutil.copy(CWD + os.sep + "Development.pfx", CWD + os.sep + "Server/Development.pfx")

shutil.copy(CWD + os.sep + ".CI-CD" + os.sep + "Key.pem", CWD + os.sep + "Server/Key.pem")
File = open(CWD + os.sep + "Server" + os.sep + "PEM.py", "w+")
Content = """\
Value = \"\"\"\\
{0}
\"\"\"
""".format(open(CWD + os.sep + ".CI-CD" + os.sep + "Key.pem", "r").read().strip())
File.write(Content)
File.close()

URLs = {
    "Documentation": "https://github.com/cloud-hybrid/backend-api",
    "Support":       "https://github.com/cloud-hybrid/backend-api",
    "Source":        "https://github.com/cloud-hybrid/backend-api",
    "Tracker":       "https://github.com/cloud-hybrid/backend-api",
}

Classifiers = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Environment :: Web Environment",
    "Intended Audience :: End Users/Desktop",
    "Intended Audience :: Developers",
    "Intended Audience :: System Administrators",
    "License :: OSI Approved :: Python Software Foundation License",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX",
    "Programming Language :: Python",
    "Topic :: Communications :: Email",
    "Topic :: Office/Business",
    "Topic :: Software Development :: Bug Tracking"
]

sys.stdout.write("Exported" + "\n")
sys.stdout.flush()

sys.stdout.write("[Backend-API]: Performing Pre-Flight Checks ➜ ")
sys.stdout.flush()

command = shlex.split("{0} -m pip check".format(sys.executable))
install = subprocess.Popen(
    args = shlex.split("{0} -m pip check".format(sys.executable)),
    shell = False,
    stdin = subprocess.DEVNULL,
    stdout = subprocess.PIPE,
    stderr = subprocess.STDOUT
)

command = shlex.split("{0} {1}/.CI-CD/Install-Certificate.py".format(sys.executable, Path))

certificate = subprocess.Popen(
    args = command,
    shell = False,
    stdin = subprocess.DEVNULL,
    stdout = subprocess.PIPE,
    stderr = subprocess.STDOUT
)

command = shlex.split("{0} -m pip install --upgrade pip".format(
    sys.executable
));

process = subprocess.Popen(
    args = command,
    shell = False,
    stdin = subprocess.DEVNULL,
    stdout = subprocess.PIPE,
    stderr = subprocess.STDOUT
)

process.wait(300)
install.wait(300)
certificate.wait(300)

if process.returncode != 0 and install.returncode == 1 and certificate.returncode != 0:
    sys.stdout.write("Error During Installation + Certificate Provisioning Process(es)" + "\n")
    exit(1)
else: time.sleep(1.0)

sys.stdout.write("(4/4), Ready" + "\n")
sys.stdout.flush()

sys.stdout.write("[Backend-API]: Checking Environment File(s) ➜ ")
sys.stdout.flush()

sys.stdout.write("Exported" + "\n")
sys.stdout.flush()

sys.stdout.write("[Backend-API]: Generating Distribution ➜ (Long-Running)" + "\n")
sys.stdout.flush()

shutil.copy(Path + os.sep + "Key.pem", Path + os.sep + "Server" + os.sep + "Development.key")

shutil.copy(Path + os.sep + "Configuration" + os.sep + "Development.conf", Path + os.sep + "Server")
shutil.copy(Path + os.sep + "Configuration" + os.sep + "Development.pfx", Path + os.sep + "Server")
shutil.copy(Path + os.sep + "Configuration" + os.sep + "Development.crt", Path + os.sep + "Server")

try:
    setuptools.setup(
        name = Name,
        version = Version,
        author = "Jacob B. Sanders",
        author_email = "jacob.sanders@cloudhybrid.io",
        description = "Cloud Nexus API Service(s)",
        project_urls = URLs,
        long_description = open(os.path.join(CWD, "README.md"), "r").read(),
        long_description_content_type = "text/markdown",
        packages = Packages(where = ".", include = [
            "Database", "Parser", "API", "Server", "Model", "Utility"
        ]) + Packages(),
        classifiers = Classifiers,
        package_data = {
            ".": ["README.md", "LICENSE"],
            "API": ["Environment.json"],
            "Server": [
                "VERSION",
                "Key.PEM",
                "Development.conf",
                "Development.pfx",
                "Development.crt",
                "Development.key"
            ]
        },
        python_requires = ">=3.8.0",
        include_package_data = True,
        install_requires = [],
        include_dirs = True,
        zip_safe = True,
        entry_points = {
            "console_scripts": [
                "backend-api=API.__main__:Runtime"
            ]
        }
    )

    Wheel = [
        Distribution + os.sep + Name.replace("-", "_") + "-" + "{0}-py3-none-any.whl".format(Version),
        Path + os.sep + Name + "-" + "{0}-py3-none-any.whl".format(Version),
        Name + "-" + "{0}-py3-none-any.whl".format(Version)
    ]

    if sys.argv[1].casefold() == "bdist_egg":
        os.system("mv ./Artifact/Distribution/*.egg Backend-API-{0}.egg".format(Version))
        sys.stdout.write("  ﬌ Generated (Egg)" + "\n")
    elif sys.argv[1].casefold() == "bdist_wheel":
        sys.stdout.write("  ﬌ Generated (Wheel)" + "\n")
        shutil.move(Wheel[0], Wheel[1])
    elif sys.argv[1].casefold() == "install":
        sys.stdout.write("  ﬌  Generated (Source-Binary)" + "\n")

        sys.stdout.write("[Backend-API]: Generating Egg ➜ (Backend-API-{0}.egg)".format(Version) + "\n")
        sys.stdout.flush()

        os.system("mv ./Artifact/Distribution/*.egg Backend-API-{0}.egg".format(Version))

        sys.stdout.write("  ﬌ Generated (Egg)" + "\n")
    else: sys.stdout.write("  ﬌ Installed (Source)" + "\n")

    sys.stdout.flush()

except Exception as Error: sys.stderr.write("\n" + "%s" % Error + "\n")

finally:
    os.remove(os.path.join(CWD, "setup.cfg"))

    os.system("rm -r -f *.egg-info")

    if Install:
        try:
            sys.stdout.write("[Backend-API]: Installing ➜ ")
            sys.stdout.flush()

            command = "{0} -m pip install certifi --force".format(
                sys.executable,
                Version.split(".")[0],
                Version.split(".")[1],
                Version.split(".")[2]
            ); Certifi = subprocess.Popen(
                args = shlex.split(command),
                shell = False,
                stdin = subprocess.PIPE,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE
            ); Certifi.wait(30)

            command = "{0} -m pip install {1}/Backend-API-{2}.{3}.{4}-py3-none-any.whl --force".format(
                sys.executable,
                CWD,
                Version.split(".")[0],
                Version.split(".")[1],
                Version.split(".")[2]
            )

            Wheeler = subprocess.Popen(
                args = shlex.split(command),
                shell = False,
                stdin = subprocess.PIPE,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE
            )

            Wheeler.wait(60 * 5)

            sys.stdout.flush()
            sys.stdout.write("Complete" + "\n")
            sys.stdout.flush()
        except subprocess.TimeoutExpired as Error:
            sys.stdout.write("[WARNING] - Wheel was Unsuccessful; Attempting" + "\n")
            sys.stdout.write("    Installation via Development Mode" + "\n")
            sys.stdout.flush()
        finally:
            Source = open(os.path.join(CWD, ".CI-CD" + os.sep + "Install-Certificate.py"))
            Contents = Source.read()
            Source.close()

            exec(compile(Contents, "Certificate", mode = "exec"))

            exit(0)
