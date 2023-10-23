#!/usr/bin/python3
"""
a Python script to export data in the JSON format
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    import json

    employee_id = argv[1]
    filename = f"{employee_id}.json"

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".\
        format(employee_id)

    user_response = requests.get(user_url)

    employee_name = user_response.json().get("name")

    employee_username = user_response.json().get("username")

    url_response = requests.get(todos_url)

    total_tasks = len(url_response.json())

    task_list = []
    completed_tasks = 0

    task_json = {}
    task_dict_list = []

    for task in url_response.json():
        task_dict = {}

        task_status = task.get("completed")
        task_name = task.get("title")

        task_dict["task"] = task_name
        task_dict["completed"] = task_status
        task_dict["username"] = employee_username

        task_dict_list.append(task_dict)

        # if task_status:
        #     task_list.append(task.get("title"))
        #     completed_tasks += 1

    task_json[employee_id] = task_dict_list

    # print("Employee {} is done with tasks({}/{}):".
    #       format(employee_name, completed_tasks, total_tasks))
    # for task in task_list:
    #     print(f"\t {task}")

    with open(filename, "w") as file_json:
        json.dump(task_json, file_json, indent=2)
