# Docker Proof of Concept for Plan of Work
## Description
A small container-based application for demoing Docker capabilities to NIFA stakeholders.

## Requirements
- Docker


## Installing and Running
* Clone and change into directory `docker-poc`
* Build the containers with command: `docker-compose up --build`
* Initialize Database: `docker-compose exec api app db init`
* Seed database with some plans: `docker-compose exec api app db reset`
* Visit application in browser: `http://localhost:8080`


## Application Breakdown
#### Client/UI - A React-based UI located in `/client` directory

### API - A Python/Flask Application in `/server`
**Blueprints** - Flask Blueprints provide a method of creating submodules for the API. Each module contains a set of routes (`views.py`) to map incoming requests to that segments of code. Models are also defined in the 

This application's modules can be found in: `server/app/blueprints/`


## Unit Tests (for API)
Unit tests are located in server/tests. There are a number of sub-directories that correspond to Flask Blueprints used in the API. 

Run all tests: `docker-compose exec api app test`

Run a test for a specific module: `docker-compose exec api app test --blueprint <blueprint-name>`

