#!/usr/bin/python3
#Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.

import requests
from sys import argv


response = requests.get('https://jsonplaceholder.typicode.com/users/' + argv[1])
dico = response.json()

response2 = requests.get('https://jsonplaceholder.typicode.com/users/' + argv[1] +'/todos')
dico2 = response2.json()

tasks_done = [task for task in dico2 if task.get('completed') == True]

print('Employee {} is done with tasks({}/{}):'.format(dico.get('name'), len(tasks_done), len(dico2)))
for task in tasks_done:
    print('\t {}'.format(task.get('title')))
