#!/usr/bin/python3
"""Gather data from an API.

This module fetches an employee's TODO list progress from the
REST API at https://jsonplaceholder.typicode.com and prints it
in a specific format to standard output.
"""
import sys

import requests


def get_employee_todo_progress(employee_id):
    """Print the TODO list progress for a given employee ID.

    Args:
        employee_id (int): the ID of the employee to look up.
    """
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get("{}/users/{}".format(base_url, employee_id))
    user = user_response.json()
    employee_name = user.get("name")

    todos_response = requests.get(
        "{}/todos".format(base_url),
        params={"userId": employee_id}
    )
    todos = todos_response.json()

    done_tasks = [task for task in todos if task.get("completed") is True]
    total_tasks = len(todos)
    number_of_done_tasks = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
