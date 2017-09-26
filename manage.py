#!/bin/bash

which django-cms &> /dev/null || . env/bin/activate
export PYTHONPATH=.
export DEBUG=TEMPLATE
export SITE_MODULE=suncha
exec django-cms "$@"
