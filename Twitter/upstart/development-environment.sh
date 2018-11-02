#!/usr/bin/evn bash

python3 run/wsgi.py

find . \( -name __pycache__ -o -name "*.pyc" \) -delete
