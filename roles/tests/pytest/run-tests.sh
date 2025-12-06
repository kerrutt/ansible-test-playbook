#!/bin/bash

# Check if the script is being run as root
if [[ $EUID -ne 0 ]]; then
    echo "ERROR: This script must be run as root." >&2
    exit 1
fi

echo "Running as root. Continuing..."

pytest test-common-role.py --html=ufw_report.html --self-contained-html

# Remove __pycache__ folders
find . -type d -name "__pycache__" -exec rm -r {} +

# Remove .pytest_cache folders
find . -type d -name ".pytest_cache" -exec rm -r {} +
