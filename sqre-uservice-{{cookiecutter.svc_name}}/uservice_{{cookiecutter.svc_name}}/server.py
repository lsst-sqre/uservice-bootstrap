#!/usr/bin/env python
"""{{ cookiecutter.svc_name}} microservice framework"""
# Python 2/3 compatibility
try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError
from apikit import APIFlask
from apikit import BackendError
from flask import jsonify


def server(run_standalone=False):
    """Create the app and then run it."""
    # Add "{{ cookiecutter.route }}" for mapping behind api.lsst.codes
    app = APIFlask(name="uservice-{{ cookiecutter.svc_name }}",
                   version="{{ cookiecutter.version }}",
                   repository="{{ cookiecutter.repository }}",
                   description="{{ cookiecutter.description }}",
                   route=["/", "{{ cookiecutter.route }}"],
                   auth={"type": "{{ cookiecutter.auth_type}}"{% if cookiecutter.auth_type != "none" %},
                         "data": {"username": "",
                                   "password": ""{% if cookiecutter.auth_type == "bitly-proxy" %},
                                   "endpoint": "https://FIXME-BACKEND-URL/oauth2/start"{% endif %} }{% endif %}}){% if cookiecutter.auth_type == "bitly-proxy" %}
    app.config["SESSION"] = None{% endif %}

    @app.errorhandler(BackendError)
    # pylint can't understand decorators.
    # pylint: disable=unused-variable
    def handle_invalid_usage(error):
        """Custom error handler."""
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    @app.route("/")
    def healthcheck():
        """Default route to keep Ingress controller happy."""
        return "OK"

    @app.route("{{ cookiecutter.route }}")
    @app.route("{{ cookiecutter.route }}/")
    # @app.route("{{ cookiecutter.route }}/<parameter>")
    # or, if you have a parameter, def route_function(parameter=None):
    def route_function():
        """
        {{ cookiecutter.description }}
        """
        # FIXME: service logic goes here{% if cookiecutter.auth_type == "bitly-proxy" %}
        # See https://sqr-015.lsst.io for details.
        # - store HTTP session in app.config["SESSION"]{% endif %}
        # - raise errors as BackendError
        # - return your results with jsonify
        # - set status_code on the response as needed
        return

    if run_standalone:
        app.run(host='0.0.0.0', threaded=True)


def standalone():
    """Entry point for running as its own executable."""
    server(run_standalone=True)


if __name__ == "__main__":
    standalone()
