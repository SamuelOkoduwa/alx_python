#!/usr/bin/python3

'''The Module'''
import requests
import sys

if __name__ == "__main":
    url = sys.argv[1]  # Get the URL from the command-line argument
    email = sys.argv[2]  # Get the email address from the command-line argument

    # Create a dictionary with the email parameter
    data = {'email': email}

    # Send a POST request to the URL with the email parameter
    response = requests.post(url, data=data)

    # Display the body of the response
    print(response.text)
