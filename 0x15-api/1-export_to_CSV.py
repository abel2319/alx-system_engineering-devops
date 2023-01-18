#!/usr/bin/python3
"""script to export data in the CSV format"""
import requests
from sys import argv

if __name__ == "__main__":
    res = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    res2 = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'
            .format(argv[1]))

    dico = res.json()

    dico2 = res2.json()

    tasks_done = [task for task in dico2 if task.get('completed') is True]

    with open(argv[1] + ".csv", "w") as file:
        for task in dico2:
            file.write('"{},"{}","{}","{}"\n'
                       .format(argv[1], dico.get('name'),
                               task.get('completed'), task.get('title')))
