#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": id}).json()
    with open("{}.csv".format(int(id)), 'w', newline='') as csv_file:
        f = ['UserID', 'Username', 'Completed', 'Title']
        wr = csv.DictWriter(csv_file, quoting=csv.QUOTE_ALL, fieldnames=f)
        wr.writeheader()
        for t in todos:
            wr.writerow({
                'UserID': id,
                'Username': username,
                'Completed': t.get('completed'),
                'Title': t.get('title')
            })
