# CMS Bootstrap for Python

A Python example project for CMS-SDK

## Requirements

- composer
- docker
- python 3.5 or higher

## Setup

1. `make install`
1. `make cms-up` will start docker containers.
1. Wait for several seconds until the conainers startup.
1. `make cms-db` for sample db migration. If it fails, try again in a few seconds.
1. `python sample.py` will run the sample code.
1. `make cms-down` for shutting down the containers.

## APIs

See [here](https://github.com/ridi/cms-sdk/tree/2.x/lib/thrift-idl) for all available APIs.