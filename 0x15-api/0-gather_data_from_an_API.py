#!/usr/bin/python3
"""
a Python script that, for a given employee ID,
returns information about his/her TO-DO list progress
"""

import requests
from sys import argv

employee_id = argv[1]

user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

user_response = requests.get(user_url)

employee_name = user_response.json().get("name")

url_response = requests.get(todos_url)

total_tasks = len(url_response.json())

task_list = []
completed_tasks = 0

for task in url_response.json():
    task_status = task.get("completed")
    if task_status:
        task_list.append(task.get("title"))
        completed_tasks += 1

print(f"Employee {employee_name} is done with tasks \
      ({completed_tasks}/{total_tasks}):")
for task in task_list:
    print(f"\t {task}")
