#!/usr/bin/python3

"""Imported Modules
"""
import requests
import sys


if len(sys.argv) < 2:
    q = ""
else:
    q = sys.argv[1]

url = "http://0.0.0.0:5000/search_user"
data = {"q": q}

response = requests.post(url, data=data)

try:
    response_json = response.json()
    if response_json:
        print(f"[{response_json['id']}] {response_json['name']}")
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")



