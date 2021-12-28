# Setup and development
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

## Setup virtual environment on Pycharm
- [Config interpreter](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#add-existing-interpreter)
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

Environment File 
```env
DATABASE_URL = 'postgresql://postgres:password@localhost/manage_student'
```

## Run source

### With commandline
```commandline
    uvicorn main:app --reload
```
### With configuration
```
- Add new configuration
- Module name: uvicorn
- Parameters: main:app --reload
```

