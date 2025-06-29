#!/bin/bash

python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
#rm -rf public

reflex init
# API_URL ya no es necesaria aquí
# API_URL=https://api.v1ct0r.dev reflex export --frontend-only
reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
deactivate


