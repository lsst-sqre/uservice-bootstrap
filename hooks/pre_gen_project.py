#!/usr/bin/env python
import string
import sys


def validate():
    """Validate Cookiecutter input."""
    # auth_type is validated by list in cookiecutter.json
    validate_svc_name("{{ cookiecutter.svc_name }}")
    # Room for improvement.


def validate_svc_name(svc_name):
    bad = False
    reason = ""
    if svc_name == "":
        bad = True
        reason = "svc_name must not be empty"
    if not bad:
        allowed_chars = string.digits + string.ascii_letters + '_'
        xtable = string.maketrans('', '')
        if svc_name.translate(xtable, allowed_chars) != "":
            bad = True
            reason = "svc_name can only contain ASCII letters, digits, and '_'"
    if not bad:
        first = svc_name[0]
        if first in string.digits:
            bad = True
            reason = "svc_name must not start with a digit"
    if bad:
        print("VALIDATION ERROR: " + reason + ".")
        sys.exit(2)


if __name__ == "__main__":
    validate()
