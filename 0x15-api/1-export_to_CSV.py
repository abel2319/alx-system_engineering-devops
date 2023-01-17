#!/usr/bin/python3
"""Python script that, using this REST API """
import requests
from sys import argv


response = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        argv[1])
response2 = requests.get('https://jsonplaceholder.typicode.com/users/' +
                         argv[1] + '/todos')

dico = response.json()
dico2 = response2.json()

tasks_done = [task for task in dico2 if task.get('completed') is True]

with open(argv[1] + ".csv", "a") as file:
    for task in dico2:
        file.write('"{},"{}","{}","{}"\n'
                   .format(argv[1], dico.get('name'),
                           task.get('completed'), task.get('title')))

"""print('Employee {} is done with tasks({}/{}):'
      .format(dico.get('name'), len(tasks_done), len(dico2)))

to_save = ''"""
