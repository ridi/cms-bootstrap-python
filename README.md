# CMS Bootstrap for Python

A Python example project for CMS-SDK.

This example uses docker images provided by [cms-docker-compose](https://github.com/ridi/cms-docker-compose). Learn more details about the docker images in the link.

> If you need Django rest framework exmaple; [click here](sample_drf_middleware/README.md)

## Requirements

- composer
- docker
- python 3.5 or higher

## Setup

1. Set up [venv](https://docs.python.org/3/library/venv.html).
    1. `python3 -m venv .venv && source ./.venv/bin/activate`
1. `make install`
1. `make cms-up` will start docker containers.
1. Wait for several seconds until the conainers startup.
1. `make cms-db` for sample db migration. If it fails, try again in a few seconds.
1. `python sample.py` will run the sample code.
    1. Or `python sample_flask.py` will run the sample flask web server, then you can browse to `http://127.0.0.1/example/home`.
1. `make cms-down` for shutting down the containers.

## APIs

See [here](https://github.com/ridi/cms-sdk/tree/2.x/lib/thrift-idl) for all available APIs.
