#!/usr/bin/python3
""" given employee ID, returns information about
his/her todo list progress. """


if __name__ == '__main__':
    import requests
    from sys import argv
    # Get name
    get = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                       format(argv[1]))
    name = get.json().get('name')
    # get list employ
    get = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                       format(argv[1]))
    data_json = get.json()
    done = total = 0
    for task in data_json:
        total += 1
        if task.get('completed'):
            done += 1
    # print
    print('Employee {} is done with tasks({}/{}):'.format(name, done, total))
    for task in data_json:
        if task.get('completed'):
            print('\t {}'.format(task.get('title')))
