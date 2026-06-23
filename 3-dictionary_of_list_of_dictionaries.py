#!/usr/bin/python3
"""Dictionary of list of dictionaries.

This module fetches TODO list data for all employees from the
REST API at https://jsonplaceholder.typicode.com and exports
every employee's tasks to a single JSON file named
todo_all_employees.json.
"""
import json

import requests


def export_all_employees_todos_to_json():
    """Export all tasks of all employees to a single JSON file."""
    base_url = "https://jsonplaceholder.typicode.com"

    users_response = requests.get("{}/users".format(base_url))
    users = users_response.json()

    todos_response = requests.get("{}/todos".format(base_url))
    todos = todos_response.json()

    all_tasks = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos
            if task.get("userId") == user_id
        ]
        all_tasks[str(user_id)] = user_tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    export_all_employees_todos_to_json()
