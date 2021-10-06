# Parser #

## Table of Contents ##

[[_TOC_]]

## Overview ##

- [ ] Update [Overview](#overview)
- [ ] Update [Async Section](#working-with-asyncronous-code)

...

## Working with Asyncronous Code ##

...

## Creating a `Parser` Python Module ##
1. Create a new Python Module
    - Example) `touch ./Parser/Test.py`
        ```python
        import os
        import sys
        import signal
        
        import typing
        
        from . import Action
        
        Integer = int
        String = str
        Float = float
        Bytes = bytes
        Array = bytearray
        List = list
        Dictionary = dict
        Tuple = tuple
        Address = memoryview
        
        Optional = typing.Optional
        
        Union = typing.Union
        
        Update = lambda Key, Value: os.environ.update({Key: Value})
        
        Environment = lambda Variable, Default = None: os.getenv(Variable, Default)
        
        class Configuration:
        """
        ...
        """
    
        def __init__(self, *argv, **kwargs):
            map(setattr, kwargs.items())
    
        @staticmethod
        def System():
            """
            Hostname Environment Configuration
            """
    
            Key: String = "NEXUS_API_UNIT_TESTING"
    
            Value: String = "%s" % 1
    
            print("Configuring Environment Unit-Testing Flag")
    
            Update(Key, Value)
    
            print("  ↳ ", "Configured Variable ... ")
            print("  - ", "Key:     {0}".format(
                Key), "\n", " -  Value:   {0}".format(
                    Environment(Key)
                ), "\n"
            )
    
        class Command(Action):
            """
            ...
            """
    
            def __call__(self, Parser, Namespace, Values: List, Options = None):
                """
                ...
                """
    
                setattr(Namespace, self.dest, lambda: Configuration.System())
    
        __all__ = [
            "Configuration"
        ]
    
        ```
1. Open `./Parser/Base.py` & Import + Compose the Module's Command.
    - Example) 
    ```python
    ...
   
    import Parser.Test as Test
   
    ...
   
    class CMD:
        ...
        
        Test: Action = Test.Configuration.Command
    ```
1. Open `./Parser/Parse.py`.
1. Optionally Add a Sub-Parser.
1. Add a [Sub]-Parser Argument(s).
    - Example)
    ```python
    Parser.add_argument("--Unit-Test", "--Test", "--UAT", "-U",
        action = Context.Test.Configuration.Command,
        default = argparse.SUPPRESS,
        dest = "Test",
        nargs = 0
    )
   ```
1. Open `./Parser/__init__.py` & Attribute `Environment` a 
   Variable `Test: ... = lambda: ...`
1. In `./Parser/Parse.py`, Add `Environment.Test()` after 
   `Arguments = Parser.parse_args(namespace = Environment)`.
