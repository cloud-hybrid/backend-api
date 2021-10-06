---
Author: Jacob B. Sanders
Description: What to include in GitLab documentation pages.
Difficulty: Intermediate
Type: Technical Documentation
Updated: 06-15-2020
---

# Regular Expression Matching #

Various RegEx Patterns for String Matching & Substitution

## Table of Contents ##

- [Regular Expression Matching](#regular-expression-matching)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Server Notations](#server-notations)
    - [VPS Naming](#vps-naming)
    - [Tags](#tags)
  - [Sources](#sources)

## Overview ##

A regular expression [2](shortened as regex or [1]regexp also referred to as rational expression)
is a sequence of characters that define a search pattern. Usually such patterns are used by
string searching algorithms for "find" or "find and replace" operations on strings, or for input
validation. It is a technique developed in theoretical computer science and formal language
theory.

It's strongly encouraged to visit [*http://www.regular-expressions.info*](http://www.regular-expressions.info/tutorial.html) for review if the User is unfamiliar with *regular expressions*.

## Server Notations ##

Servers make up a large amount of resources in the Cloud (however, are far from the only types of resources); consquently, **Server Naming** & *Tagging* -- special attributes that further define the resource -- largely contribute(s) to [3]automata.

### VPS Naming ###

*Virtual Private Server* (VPS) naming is represented via the following notation:

**`[Server-Name]-[US|EU]-[Central|East|West|North|South]-[Number]`**

| Tag | Notation | Expression | Example | Reference |
|:-:|:-:|:-:|:-:|:-:|
| **Environment** | **`[Production|Development|Staging]`** |  |  |  |
| **Name** | **`[Server-Name]-[US|EU]-[Central|East|West|North|South]-[Number]`** | `^([a-zA-Z-]*)-(US|EU)-(Central|East|West|North|South)-([0-9]*)` | * `Mordhau-US-Central-1` * | [4][Link](https://regex101.com/r/mxyHbE/1) |
|  |  |  |  |  |

Where `Server-Name` is an easy to read, yet unique identifier related to the server's name and function -- space delimited with `-` (hyphens). Following includes *US* or `EU`, `US`, *`EU`* and *`US`*-specific `region`, and then number representing the server-function count.

*`Mordhau-US-Central-1`*

```python
#!/usr/bin/env python3

# -*-  Coding: UTF-8  -*- #
# -*-  System: Linux  -*- #
# -*-  Usage:  *.PY   -*- #

import re
import sys
import uuid

TAB = lambda depth: sys.stdout.write("\b".join(" " * 4 * depth))

regularExpression = {
    "Environment": (
        r"(Production|Development|Staging)",
        "Production"
    ), "Server-Name": (
        r"^([a-zA-Z-]*)-(US|EU)-(Central|East|West|North|South)-([0-9]*)",
        "Mordhau-US-Central-1"
    ), "UUID": (
        r"^([a-zA-Z-]*)-(US|EU)-(Central|East|West|North|South)-([0-9]*)",
        "{}-{}".format("x", uuid.uuid4())
    )
}

for Tag, Expression in regularExpression.items():
    string = Expression[-1]
    regex = Expression[0]

    matches = re.finditer(regex, string, re.MULTILINE)

    print("Tag: {}".format(Tag))
    for index, match in enumerate(matches, start = 1):
        print("{} Match {} was found at {}-{}: {}".format(
            TAB()
            index,
            match.start(),
            match.end(),
            match.group()
        ))
        for groupIndex in range(0, len(match.groups())):
            groupIndex = groupIndex + 1

            print("{} Group {} found at {}-{}: {}".format(
                groupIndex,
                match.start(groupIndex),
                match.end(groupIndex),
                match.group(groupIndex)
            ))
```

### Tags ###

```python
#!/usr/bin/env python3

# -*-  Coding: UTF-8  -*- #
# -*-  System: Linux  -*- #
# -*-  Usage:  *.PY   -*- #

import re

regex = {
    "Environment": r"(Production|Development|Staging)",
    "Server-Name": r"^([a-zA-Z-]*)-(US|EU)-(Central|East|West|North|South)-([0-9]*)",
    ""

test_str = "Mordhau-US-Central-1"

matches = re.finditer(regex, test_str, re.MULTILINE)

for index, match in enumerate(matches, start = 1):
    print("Match {} was found at {}-{}: {}".format(
        index,
        match.start(),
        match.end(),
        match.group()
    )); for groupIndex in range(0, len(match.groups())):
        groupIndex = groupIndex + 1

        print("Group {} found at {}-{}: {}".format(
            groupIndex,
            match.start(groupIndex),
            match.end(groupIndex),
            match.group(groupIndex)
        ))
```

---

## Sources ##

- [^1]: [Notation Tutorial](http://www.regular-expressions.info/tutorial.html)
- [^2]: [Oxford Journal](https://books.google.com/books?id=yl6AnaKtVAkC&pg=PA754#v=onepage&q&f=false)
- [^3]: [Automata Theory](https://en.wikipedia.org/wiki/Automata_theory)
- [^4]: [RegEx Online Tool](https://regex101.com/r/mxyHbE/1)
