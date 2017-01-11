[![Build Status](https://travis-ci.org/lsst-sqre/uservice-{{ cookiecutter.svc_name }}.svg?branch=master)](https://travis-ci.org/lsst-sqre/uservice-{{ cookiecutter.svc_name }})

# sqre-uservice-{{ cookiecutter.svc_name }}

LSST DM SQuaRE microservice wrapper.  TODO

## Usage

`sqre-uservice-{{ cookiecutter.svc_name}}` will run standalone on port
5000 or under `uwsgi`.  It responds to the following routes:

### Routes

* `/`: returns `OK` (used by GCE Ingress healthcheck)

* `/{{ cookiecutter.svc_name}}`: TODO

### Returned Structure

The returned structure is JSON.  TODO.
