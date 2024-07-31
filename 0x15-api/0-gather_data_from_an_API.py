#!/usr/bin/python3
"""Implementation of a python script that returns information
    using a REST api"""
import requests
import sys


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
    done = [todo for todo in todos_data if todo.get
                  ("completed")]
    done_tasks = len(done)

    # Display progress
    print(f"""Employee {employee_name} is done with tasks({done_tasks}/{total}):""")
    for task in done:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
