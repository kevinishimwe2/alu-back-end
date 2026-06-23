#!/usr/bin/python3
"""Export to JSON.

This module fetches an employee's TODO list data from the
REST API at https://jsonplaceholder.typicode.com and exports
all of that employee's tasks to a JSON file named USER_ID.json.
"""
import requests
import json
import sys




def export_employee_todos_to_json(employee_id):
    """Export all tasks of a given employee to a JSON file.

    Args:
        employee_id (int): the ID of the employee to look up.
    """
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get("{}/users/{}".format(base_url, employee_id))
    user = user_response.json()
    username = user.get("username")

    todos_response = requests.get(
        "{}/todos".format(base_url),
        params={"userId": employee_id}
    )
    todos = todos_response.json()

    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        for task in todos
    ]

    all_tasks = {str(employee_id): tasks}

    filename = "{}.json".format(employee_id)
    with open(filename, "w") as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    export_employee_todos_to_json(employee_id)
