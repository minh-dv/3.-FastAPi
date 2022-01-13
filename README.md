# Setup and development for Api and Auth Service
- [Prerequisite](#prerequisite)
- [Setup virtual environment on Pycharm](#setup-virtual-environment-on-pycharm)
- [Installation](#installation)
- [Configuration](#configuration)
- [Run source](#run-source)
  - [With commandline](#with-commandline)
  - [With configuration](#with-configuration)

##  Prerequisite

Make sure you have the following installed:

- [Python](https://www.python.org/downloads/release/python-390/) (at least version 3.9)
- [Postgresql](https://www.postgresql.org/download/) (Download and setup Database)

## Setup virtual environment on Pycharm
- [Config interpreter](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#add-existing-interpreter)
  (We will add interpreter for each service)
- Install plugins EnvFile
```bash
  Setting > Plugins > find "EnvFile" > Install
```

## Installation
Install python package and libraries:
```bash
  pip install -r requirements.txt
```

## Configuration
Make sure to run resource with envFile

Environment File (.env)
```env
DATABASE_URL = 'postgresql://postgres:password@localhost/manage_student'

with:
  postgres: User of databse
  password: Password of database
  manage_student: Name of database
```

## Run source
Run source with Api Service or Auth Service is the same way
### With commandline
- With Api Service
```commandline
    uvicorn main:app --reload --port 9091
```

- With Auth Service
```commandline
    uvicorn main:app --reload --port 9092
```
### With configuration
Add Run/Debug configurations

- With Api Service
```
- Add new configuration
- Module name: uvicorn
- Parameters: main:app --reload --port 9091
```

- With Auth Service
```
- Add new configuration
- Module name: uvicorn
- Parameters: main:app --reload --port 9092
```
Reference [here](https://www.jetbrains.com/help/pycharm/run-debug-configuration.html#share-configurations).

