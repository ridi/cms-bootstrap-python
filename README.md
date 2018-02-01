# CMS Bootstrap for Python

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
