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
        # Yes, hideously inefficient, but svc_name will be short anyway
        # Gets around both compiling a regexp and the differences in
        #  translate() between Python 2 and 3.
        for chr in svc_name:
            if chr not in allowed_chars:
                bad = True
                reason = "svc_name can only contain digits, ascii letters, "
                reason += "and underscore"
                break
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
