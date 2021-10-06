# Packaging Applications #

## Essential Files ##

### `setup.py` - Command-Line Management  ###
The most important file is `setup.py` which exists at the root of your project directory. For an 
example, see the setup.py in the PyPA sample project.

setup.py serves two primary functions:

It’s the file where various aspects of your project are configured. The primary feature of setup.py 
is that it contains a global setup() function. The keyword arguments to this function are how 
specific details of your project are defined. The most relevant arguments are explained in the 
section below.

It’s the command line interface for running various commands that relate to packaging tasks. To get 
a listing of available commands, run python setup.py --help-commands.
