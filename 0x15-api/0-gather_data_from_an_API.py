#!/usr/bin/python3
"""Python script that, using this REST API """
import requests
import sys

if __name__ == "__main__":
    """entry"""
    response = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(sys.argv[1]))
    response2 = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'
            .format(sys.argv[1]))

    dico = response.json()
    dico2 = response2.json()

    tasks_done = [task for task in dico2 if task.get('completed') is True]

    print('Employee {} is done with tasks({}/{}):'
          .format(dico.get('name'), len(tasks_done), len(dico2)))

    for task in tasks_done: print('\t {}'.format(task.get('title')))
