#!/usr/bin/python3
"""Implementation of a python script that returns information
    using a REST api"""
import requests
import sys
import csv


def get_employee_todo_progress(employee_id):
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Endpoint for user and todos
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch user data
    user_response = requests.get(user_url)

    # Fetch todos data
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error: Could not fetch TODOS data.")
        return

    # Parse JSON data
    user_data = user_response.json()
    todos_data = todos_response.json()

    # Extract necessary information
    employee_name = user_data.get("name")
    total = len(todos_data)
    done = [todo for todo in todos_data if todo.get("completed")]
    d_tasks = len(done)

    # Display progress
    print(f"Employee {employee_name} is done with tasks({d_tasks}/{total}):")
    for task in done:
        print(f"\t {task.get('title')}")

    # Export to CSV
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                employee_id,
                employee_name,
                task.get("completed"),
                task.get("title")
            ])
    print(f"Data exported to {csv_filename}")


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
