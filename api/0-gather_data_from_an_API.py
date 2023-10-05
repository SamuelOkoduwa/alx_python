#!/usr/bin/python3

import requests
import sys

def get_employee_data(employee_id):
    #	The API enpoints
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"{base_url}/users/{employee_id}"
    todos_endpoint = f"{base_url}/todos?userId={employee_id}"
    
    # fetching employee data 
    user_response = requests.get(user_endpoint)
    todos_response = requests.get(todos_endpoint)
    
    # Checking if the requests were successful
    if user_response.status_code != 200:
        print(f"Error: Could not retrieve employee data for ID {employee_id}")
        
    if todos_response.status_code != 200:
        print(f"Error: Could not retrieve Todo list for ID {employee_id}")
    
    # the file in json format
    user_data = user_response.json()
    todos_data = todos_response.json()
    
    # calculating the number of completed and total task
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for task in todos_data if task["completed"])
    
    # printing employee's progress
    print(f"Employee {user_data['name']} is done with tasks({completed_tasks}/{total_tasks}):")
    for task in todos_data:
        if task["completed"]:
            print(f"\t{task['title']}")
            
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_data(employee_id)
        
    