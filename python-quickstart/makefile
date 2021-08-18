SHELL=bash

APPLICATION_NAME=python-quickstart

ifeq ($(OS),Windows_NT)
	SYSTEM_PYTHON=py -3.9
	VENV_HOME=./venv/Scripts
else
	SYSTEM_PYTHON=python3
	VENV_HOME=./venv/bin
endif

help:
	@echo "init-venv:						Sets up the project, preparing the Python venv and installs dependencies."
	@echo "update-dependencies:				Update all installed dependencies."
	@echo "ut:								Run unittests."


create-venv:
	${SYSTEM_PYTHON} -m venv venv

install-dependencies:
	${VENV_HOME}/pip3 install -r requirements.txt

init-venv: create-venv install-dependencies

ut:
	pytest test

clean:
	test ! -d build || rm -r build