#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.

This script takes an employee ID as a command-line argument and fetches
the corresponding user information and to-do list from the JSONPlaceholder API.
It then prints the tasks completed by the employee.
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Fetch and display the todo list progress of an employee.

    Args:
        employee_id (int): The ID of the employee.
    """
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # Fetch todos for the user
    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params=params).json()

    # Filter completed tasks
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Display employee's task completion progress
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    for complete in completed:
        print("\t {}".format(complete))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
