#!/usr/bin/python3
""" export data in the CSV format. """

if __name__ == '__main__':
    import csv
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
    with open('{}.csv'.format(argv[1]), mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for task in data_json:
            csv_writer.writerow([argv[1], username, task.get('completed'),
                                 task.get('title')])
    # print
"""     print('Employee {} is done with tasks({}/{}):'.format(name, done, total))
    for task in data_json:
        if task.get('completed'):
            print('\t {}'.format(task.get('title'))) """
