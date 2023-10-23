#!/usr/bin/python3
"""
a Python script to export data in the JSON format
"""

if __name__ == "__main__":
    import requests
    import json

    filename = "todo_all_employees.json"

    final_dict = {}

    for employee_id in range(1, 11):
        user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".\
            format(employee_id)

        user_response = requests.get(user_url)

        employee_username = user_response.json().get("username")

        url_response = requests.get(todos_url)

        task_dict_list = []

        for task in url_response.json():
            task_dict = {}

            task_status = task.get("completed")
            task_name = task.get("title")

            task_dict["username"] = employee_username
            task_dict["task"] = task_name
            task_dict["completed"] = task_status

            task_dict_list.append(task_dict)

        final_dict[employee_id] = task_dict_list

    with open(filename, "w") as file_json:
        json.dump(final_dict, file_json, indent=2)
