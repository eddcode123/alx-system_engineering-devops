#!/usr/bin/python3
""" This python script uses request to retrieve data from api """
import requests
import sys


if __name__ == '__main__':
    """ function uses get request to get info """
    # get user_data
    url = 'https://jsonplaceholder.typicode.com/'
    user = f'/users/{sys.argv[1]}'
    req = requests.get(f'{url}' + f'{user}')
    user_data = req.json()
    print(f'Employee {user_data.get("name")} is done with tasks ', end='')

    # get todos
    todos = f'/todos/{sys.argv[1]}'
    req_1 = requests.get(f'{url}' + f'{todos}')
    tasks = req_1.json()
    completed_tasks = [task.get('title') for task in tasks if task.get('complete') is True]
    print(f'({len(completed_tasks)}/{len(tasks)}):')
    for task in completed_tasks:
        print(f"\t{task.get('title')}")
