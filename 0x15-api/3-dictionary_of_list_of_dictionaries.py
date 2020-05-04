#!/usr/bin/python3
""" export data in the CSV format. """

if __name__ == '__main__':
    import json
    import requests
    from sys import argv

    all_id = set()
    get = requests.get('https://jsonplaceholder.typicode.com/posts')
    data_json = get.json()
    for user in data_json:
        all_id.add(user.get('userId'))
    # Export format dic
    json_dict = {}
    for user in all_id:
        # Get employ
        get = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                           format(user))
        username = get.json().get('username')

        get = requests.get('https://jsonplaceholder.typicode.com/' +
                           'todos?userId={}'.format(user))
        data_json = get.json()

        json_dict['{}'.format(user)] = []
        for task in data_json:
            json_dict['{}'.format(user)].append({
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': username
            })
    # Exporting json
    filename = 'todo_all_employees.json'
    with open(filename, 'w') as outfile:
        json.dump({int(x): json_dict[x] for x in json_dict.keys()},
                  outfile, sort_keys=True)
