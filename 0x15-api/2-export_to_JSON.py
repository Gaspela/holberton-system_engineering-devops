#!/usr/bin/python3
""" export data in the CSV format. """

if __name__ == '__main__':
    import json
    import requests
    from sys import argv
    # Get username
    get = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                       format(argv[1]))
    username = get.json().get('username')
    # get list employ
    get = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                       format(argv[1]))
    data_json = get.json()
    export = {}
    export['{}'.format(argv[1])] = []
    for task in data_json:
        export['{}'.format(argv[1])].append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': username
        })
    with open('{}.json'.format(argv[1]), 'w') as outfile:
        json.dump(export, outfile)
    # print
""" print('Employee {} is done with tasks({}/{}):'.format(name, done, total))
    for task in data_json:
        if task.get('completed'):
            print('\t {}'.format(task.get('title'))) """
