'''Importing modules'''
import json
import requests
import sys


'''
def get_all_employee_data():
    # Define API endpoints
    base_url = "https://jsonplaceholder.typicode.com/users"
    
    # Initialize a dictionary to store data for all employees
    all_employee_data = {}

    # Fetch data for all employees
    user_response = requests.get(base_url)

    # Check if the request was successful
    if user_response.status_code != 200:
        print("Error: Could not retrieve employee data")
        return

    users_data = user_response.json()

    for user in users_data:
        # Fetch TODO list for each employee
        employee_id = user["id"]
        todos_endpoint = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
        todos_response = requests.get(todos_endpoint)

        if todos_response.status_code != 200:
            print(f"Error: Could not retrieve TODO list for employee ID {employee_id}")
            continue

        todos_data = todos_response.json()

        # Store data for this employee
        employee_username = user['username']
        employee_tasks = [{"username": employee_username, "task": task['title'], "completed": task['completed']} for task in todos_data]

        # Append employee tasks to the dictionary using their user ID as the key
        all_employee_data[str(employee_id)] = employee_tasks

    # Export data to JSON
    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as json_file:
        json.dump(all_employee_data, json_file, indent=4)  # Use indent for pretty formatting

if __name__ == "__main__":
    get_all_employee_data()
'''

"""Accessing a REST API for todo lists of employees"""

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 3-dictionary_of_list_of_dictionaries.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Fetch user data
    user_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    user_data = user_response.json()
    username = user_data["username"]

    # Fetch tasks data for the given user
    tasks_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    tasks_data = tasks_response.json()

    # Create a dictionary to store tasks for all users
    all_tasks = {}

    # Iterate through tasks to organize them by user
    for task in tasks_data:
        user_id = task["userId"]
        if user_id not in all_tasks:
            all_tasks[user_id] = []

        task_data = {
            "username": username,
            "task": task["title"],
            "completed": task["completed"],
        }

        all_tasks[user_id].append(task_data)

    # Export the data to a JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)

print('User ID and Tasks output: OK')