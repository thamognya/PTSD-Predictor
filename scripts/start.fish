#!/bin/fish

python3 -m venv env/
source ./env/bin/activate.fish
source ./.env-fish
pip install -r ./requirements.txt
echo "start working"