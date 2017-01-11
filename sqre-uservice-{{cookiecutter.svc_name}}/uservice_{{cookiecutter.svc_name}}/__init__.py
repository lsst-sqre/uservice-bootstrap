#!/usr/bin/env python
"""SQuaRE {{ cookiecutter.svc_name }} proxy (api.lsst.codes-compliant)"""
from .server import server, standalone
__all__ = ["server", "standalone"]
