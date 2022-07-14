#!/bin/fish

python3 -m venv env/
source ./env/bin/activate
source ./.env
pip install -r ./requirements.txt
echo "start working"