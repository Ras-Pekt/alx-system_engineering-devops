#!/usr/bin/python3
"""
a Python script to export data in the CSV format
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    import csv

    employee_id = argv[1]
    filename = f"{employee_id}.csv"

    csv_file = open(filename, 'w')
    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

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

    for task in url_response.json():
        task_status = task.get("completed")
        task_name = task.get("title")

        csv_writer.writerow([
            employee_id,
            employee_username,
            task_status,
            task_name
        ])

        if task_status:
            task_list.append(task.get("title"))
            completed_tasks += 1

    csv_file.close()

    print("Employee {} is done with tasks({}/{}):".
          format(employee_name, completed_tasks, total_tasks))
    for task in task_list:
        print(f"\t {task}")
