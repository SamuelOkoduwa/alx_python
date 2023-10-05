'''Importing modules'''
import json
import requests


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
