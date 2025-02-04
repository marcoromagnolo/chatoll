#!/bin/bash

source ./venv/bin/activate

./venv/bin/python --version
./venv/bin/pip install -r requirements.txt
./venv/bin/python app.py -- chatoll > ./log/socialshare.out 2>&1 &
