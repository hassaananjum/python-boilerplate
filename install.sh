#!/bin/bash
pip3 install virtualenv
virtualenv env
source env/bin/activate

requirements="./Requirements.txt"
pip3 install -r $requirements
cp -n "./config/config.sample.py" "./config/config.py"
source env/bin/activate