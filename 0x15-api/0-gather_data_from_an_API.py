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
    # Define the base URLs for the API
    users_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch the employee's information
    user_response = requests.get(users_url)
    if user_response.status_code != 200:
        print(f"Failed to fetch user data: {user_response.status_code}")
        return

    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch the employee's TODO list
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Failed to fetch TODO data: {todos_response.status_code}")
        return

    todos_data = todos_response.json()

    # Calculate the number of completed and total tasks
    total_tasks = len(todos_data)
    done_tasks = [todo for todo in todos_data if todo['completed']]
    number_of_done_tasks = len(done_tasks)

    # Print the progress report
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
