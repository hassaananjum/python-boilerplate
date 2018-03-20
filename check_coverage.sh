#!/bin/bash

coverage run -m unittest tests/index_test.py
coverage report -m