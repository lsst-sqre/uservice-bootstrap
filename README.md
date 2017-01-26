[![Build Status](https://travis-ci.org/lsst-sqre/uservice-bootstrap.svg?branch=master)](https://travis-ci.org/lsst-sqre/uservice-bootstrap)

# sqre-uservice-bootstrap

LSST DM SQuaRE cookiecutter template for writing api.lsst.codes
microservices, as described in https://sqr-015.lsst.io .

## Usage

    pip install cookiecutter
    cookiecutter https://github.com/lsst-sqre/uservice-bootstrap.git
	
Then answer the prompted questions, and follow the instructions on your
screen.

### Versioning

There are three places the service version number appears.  One is in
`setup.py`, one is in `Dockerfile`, and one is in `server.py`.  Although
these will all be created with the same value, it is the developer's
responsibility to keep them synchronized as the version increments.
Note that the Docker version *can* be updated as a build-time
argument; nevertheless, it is preferable to update it in all three
files. 
