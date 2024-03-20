#!/usr/bin/python3
"""Exports to-do list of user in a specified foramt to json file """
import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": id}).json()

    file_json = {
        f'{id}': [
            {
                'task': f"{t.get('title')}",
                'completed': f"{t.get('completed')}",
                'username': f"{username}"
            }
            for t in todos
        ]
    }

    with open(f'{id}.json', 'w') as json_file:
        json.dump(file_json, json_file)
