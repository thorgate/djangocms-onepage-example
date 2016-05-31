# ENV defaults to local (so that requirements/local.txt are installed), but can be overridden
#  (e.g. ENV=production make setup).
ENV ?= local
# PYTHON specifies the python binary to use when creating virtualenv
PYTHON ?= python3.4


all: help

help:
	@echo "make setup   - Sets up the project in your local machine"
	@echo "               This includes copying PyCharm files, creating virtualenv, installing requirements,"
	@echo "               creating local settings file, doing db migrations and installing npm packages."
	@echo "make pycharm - Copies default PyCharm settings (unless they already exist)"


setup: pycharm venv onepager/settings/local.py
	venv/bin/pip install -r requirements/$(ENV).txt
	cd onepager && ../venv/bin/python manage.py migrate
	cd onepager && npm install --python=python2.7


pycharm: .idea


.idea:
	mkdir -p .idea
	cp -R .idea_template/* .idea/

venv:
	virtualenv -p $(PYTHON) venv

onepager/settings/local.py:
	cp onepager/settings/local.py.example onepager/settings/local.py
