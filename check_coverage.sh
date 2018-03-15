#!/bin/bash

coverage run -m unittest webapp/tests/hello_test.py
coverage report -m