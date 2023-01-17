#!/usr/bin/python3
"""script to export data in the CSV format"""
import requests
from sys import argv


response = requests.get('https://jsonplaceholder.typicode.com/users/' +
                        argv[1])
response2 = requests.get('https://jsonplaceholder.typicode.com/users/' +
                         argv[1] + '/todos')

dico = response.json()
dico2 = response2.json()


dict_save = {}
dict_save[argv[1]] = []
tmp = {}

for task in dico2:
    """tmp['task'] = task.get('title')

    if task.get('completed'):
        tmp['completed'] = 'true'
    else:
        tmp['completed'] = 'false'
    print(tmp.get('completed'))
    tmp['username'] = dico.get('name')"""
    dict_save[argv[1]].append({'task': task.get('title'),
                               'completed': 'false' if task.get('completed')
                               else 'true',
                               'username': dico.get('name')
                               })

with open(argv[1] + ".json", "a") as file:
    file.write(str(dict_save))
