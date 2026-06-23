#!/usr/bin/python3
"""Export to CSV.

This module fetches an employee's TODO list data from the
REST API at https://jsonplaceholder.typicode.com and exports
all of that employee's tasks to a CSV file named USER_ID.csv.
"""
import csv
import json
import sys
import urllib.request


def export_employee_todos_to_csv(employee_id):
    """Export all tasks of a given employee to a CSV file.

    Args:
        employee_id (int): the ID of the employee to look up.
    """
    base_url = "https://jsonplaceholder.typicode.com"

    with urllib.request.urlopen(
            "{}/users/{}".format(base_url, employee_id)) as response:
        user = json.loads(response.read().decode("utf-8"))
    username = user.get("username")

    with urllib.request.urlopen(
            "{}/todos?userId={}".format(base_url, employee_id)) as response:
        todos = json.loads(response.read().decode("utf-8"))

    filename = "{}.csv".format(employee_id)
    with open(filename, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    export_employee_todos_to_csv(employee_id)
