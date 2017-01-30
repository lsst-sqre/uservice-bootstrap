#!/usr/bin/env python
"""SQuaRE {{ cookiecutter.svc_name }} microservice (api.lsst.codes-compliant).
"""
from .server import server, standalone
__all__ = ["server", "standalone"]
