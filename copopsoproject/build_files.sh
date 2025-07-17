#!/bin/bash
# Build script for Vercel

# Create necessary directories
mkdir -p api
mkdir -p staticfiles

# Install dependencies
pip install -r requirements.txt

# Create a clean database
python3.9 manage.py makemigrations
python3.9 manage.py migrate

# Collect static files
python3.9 manage.py collectstatic --noinput

# Make sure the script passes even if no static files are collected
exit 0 