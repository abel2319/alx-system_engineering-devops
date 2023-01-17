#!/usr/bin/python3
"""script to export data in the CSV format"""
import requests


response = requests.get('https://jsonplaceholder.typicode.com/users/')
dico = response.json()

response2 = requests.get('https://jsonplaceholder.typicode.com/users/todos')

dico2 = response2.json()

print(dico2)

"""dict_save = {}
dict_save[argv[1]] = []

for task in dico2:
    'tmp['task'] = task.get('title')

    if task.get('completed'):
        tmp['completed'] = 'true'
    else:
        tmp['completed'] = 'false'
    print(tmp.get('completed'))
    tmp['username'] = dico.get('name')'
    dict_save[argv[1]].append({'task': task.get('title'),
                               'completed': 'false' if task.get('completed')
                               else 'true',
                               'username': dico.get('name')
                               })

with open("todo_all_employees.json", "a") as file:
    file.write(json.dumps(dict_save))"""
