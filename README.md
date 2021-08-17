# Python-Quickstart-Guide

A basic guide helping trying to help you find your way in Python3.

## Guide

A general guide going over several Python topics can be found in the `PythonGuide.md`file.

## HelloWorld project

A sample HelloWorld project can be studied in the corresponding directory. The project contains several files / directories:

- src : contains a HelloWorld script.
- test : contains tests for the HelloWorld script.
- requirements : sum of the used dependencies of the project.
- makefile : providing a quick setup of venv and installing dependencies.

### Makefile

A makefile is included allowing certain functions like:

- Setting up the project and creating a project specific venv.
- Run tests.
- Update already installed dependencies.

### Dependencies

Dependencies are defined in a requirements.txt file. When setting up the project for the first time, dependencie are installed using pip.

When installing additional dependencies use your venv pip to install them. Once installed, you can export them to the requirements file by using the following command:  ./venv/bin/pip3 freeze > requirements.txt

### Tests

Tests run by using Pytest.
