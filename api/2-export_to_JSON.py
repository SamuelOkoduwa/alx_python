'''#!/usr/bin/python3

# Imported Modules

# json file format
import json	
# used to make http request
import requests
#used to access command line arguments	
import sys	

def get_employee_data(employee_id):
    # Define API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"{base_url}/users/{employee_id}"
    todos_endpoint = f"{base_url}/todos?userId={employee_id}"

    # Fetch employee data
    user_response = requests.get(user_endpoint)
    todos_response = requests.get(todos_endpoint)

    # Check if the requests were successful
    if user_response.status_code != 200:
        print(f"Error: Could not retrieve employee data for ID {employee_id}")
        return
    if todos_response.status_code != 200:
        print(f"Error: Could not retrieve TODO list for ID {employee_id}")
        return

    user_data = user_response.json()
    todos_data = todos_response.json()

    # Calculate the number of completed and total tasks
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for task in todos_data if task["completed"])

    # Print the employee's progress
    print(f"Employee {user_data['name']} is done with tasks({completed_tasks}/{total_tasks}):")

    # Export data to JSON
    json_filename = f"{employee_id}.json"
    user_tasks = [{"task": task['title'], "completed": task['completed'], "username": user_data['username']} for task in todos_data]
    user_data_json = {str(employee_id): user_tasks}
    
    with open(json_filename, 'w') as json_file:
        json.dump(user_data_json, json_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_JSON.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_data(employee_id)
'''

# Import necessary libraries
import requests  # Used to make HTTP requests to the API
import json      # Used to work with JSON data
import sys       # Used to access command-line arguments

def get_employee_info(employee_id):
    """
    Retrieves employee information and their TODO list from a REST API,
    then exports the data to a JSON file.

    Args:
        employee_id (int): The ID of the employee whose data is to be retrieved.

    Returns:
        None
    """
    # Define API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"{base_url}/users/{employee_id}"
    todos_endpoint = f"{base_url}/users/{employee_id}/todos"

    # Get employee information
    response = requests.get(user_endpoint)
    user_data = response.json()
    user_id = user_data.get("id")
    user_name = user_data.get("username")

    # Get TODO list for the employee
    response = requests.get(todos_endpoint)
    todos_data = response.json()

    # Create a JSON file for the user
    filename = f"{user_id}.json"

    tasks = []
    for task in todos_data:
        task_info = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user_name
        }
        tasks.append(task_info)

    user_tasks = {str(user_id): tasks}

    with open(filename, 'w') as json_file:
        json.dump(user_tasks, json_file, indent=4)

    print(f"JSON file '{filename}' has been created successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_and_export_to_json.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        # Ensure employee_id is an integer
        employee_id = int(employee_id)
        get_employee_info(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")