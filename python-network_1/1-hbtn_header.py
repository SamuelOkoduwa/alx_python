#!/usr/bin/python3

"""Importing the modules
"""
import requests
import sys


url = sys.argv[1]  # Get the URL from the command-line argument

response = requests.get(url)
    
# Display the X-Request-Id header if it exists
x_request_id = response.headers.get("X-Request-Id")
print(x_request_id)
 
if __name__ == "__main":
    url = sys.argv[1]  # Get the URL from the command-line argument

    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get the value of the "X-Request-Id" header from the response
        request_id = response.headers.get("X-Request-Id")
        
        if request_id is not None:
            print(request_id)
            
	
