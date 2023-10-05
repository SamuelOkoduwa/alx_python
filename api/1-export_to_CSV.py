# #!/usr/bin/python3
import csv
import requests
import sys

'''
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
'''


def get_employee_info(employee_id):
    """
    Retrieves employee information and their TODO list from a REST API,
    then exports the data to a CSV file.

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

    # Create a CSV file for the user
    filename = f"{user_id}.csv"

    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for task in todos_data:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": user_name,
                "TASK_COMPLETED_STATUS": task.get("completed"),
                "TASK_TITLE": task.get("title")
            })

    print(f"CSV file '{filename}' has been created successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_and_export_to_csv.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        # Ensure employee_id is an integer
        employee_id = int(employee_id)
        get_employee_info(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")