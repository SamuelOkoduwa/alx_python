#!/usr/bin/python3

"""Imported Modules"""
import requests
import sys

url = sys.argv[1]  # Get the URL from the command-line argument

response = requests.get(url)

print(response.text)

if response.status_code >= 400:
	print(f"Error code: {response.status_code}")