#!/bin/bash --posix

Random () { return "$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 32 ; echo '')"; } \
    && export Random