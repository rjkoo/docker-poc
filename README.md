# Docker Proof of Concept for Plan of Work
## Description
A small container-based application for demoing Docker capabilities to NIFA stakeholders.

## Requirements
- Docker


## Building and Intstalling
* Clone and change into directory `docker-poc`
* Build the containers with command: `docker-compose up --build`
* Initialize Database: `docker-compose exec api app db init`
* Seed database with some plans: `docker-compose exec api app db reset`
* Visit application in browser: `http://localhost:8080`
