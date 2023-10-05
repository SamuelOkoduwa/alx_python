# #!/usr/bin/python3

import requests
import csv
import sys

def get_employee_data(employee_id):
    # Define API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"{base_url}/users/{employee_id}"
    todos_endpoint = f"{base_url}/todos?userId={employee_id}"

    # Fetching employee data
    user_response = requests.get(user_endpoint)
    todos_response = requests.get(todos_endpoint)

    # Checking if the requests were successful
    if user_response.status_code != 200:
        print(f"Error: Could not retrieve employee data for ID {employee_id}")
        return
    if todos_response.status_code != 200:
        print(f"Error: Could not retrieve TODO list for ID {employee_id}")
        return
	# The file in json format
    user_data = user_response.json()
    todos_data = todos_response.json()

    # Creating a CSV file for the employee
    csv_file_name = f"{employee_id}.csv"
    with open(csv_file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Writing the header row
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Writing each task as a row in the CSV
        for task in todos_data:
            csv_writer.writerow([user_data['id'], user_data['name'], task['completed'], task['title']])

    print(f"Data exported to {csv_file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_CSV.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_data(employee_id)
