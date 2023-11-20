#!/usr/bin/python3
"""Lists states in database"""
from sys import argv
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306, host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT cities.id, cities.name, states.name FROM cities JOIN\
    states ON cities.state_id = states.id;')

    queried = cursor.fetchall()
    for i in queried:
        print(i)

    cursor.close()
    db.close()
