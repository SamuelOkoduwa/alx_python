#!/usr/bin/python3

"""The imported module
"""

import requests
import sys

# A Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
username = sys.argv[1]
access_token = sys.argv[2]

# Construct the URL for the GitHub API to fetch user details
url = f"https://api.github.com/user"

# Set up Basic Authentication with your username and personal access token
auth = (username, access_token)

# Send a GET request to the GitHub API using Basic Authentication
response = requests.get(url, auth=auth)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    user_info = response.json()
    user_id = user_info["id"]
    print(user_id)
else:
    print("Failed to fetch user information. Check your credentials.")

