#!/usr/bin/env python
import sys


def validate():
    """Validate Cookiecutter input."""
    validate_auth_type()
    # Room for improvement.


def validate_auth_type():
    authtype = "{{ cookiecutter.auth_type }}"
    okauths = ["none", "basic", "bitly-proxy"]
    if authtype not in okauths:
        print("Bad auth_type '%s'; must be one of %r." % (authtype, okauths))
        sys.exit(2)

if __name__ == "__main__":
    validate()
