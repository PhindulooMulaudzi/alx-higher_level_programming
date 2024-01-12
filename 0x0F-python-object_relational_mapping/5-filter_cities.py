#!/usr/bin/python3
"""Lists states in database"""
from sys import argv
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306, host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT cities.name FROM cities JOIN states on\
    cities.state_id = states.id WHERE states.name = %s', (argv[4], ))

    queried = cursor.fetchall()
    countula = 0
    for i in queried:
        if countula is not 0:
            print(', ', end='')
        print('%s' % i, end='')
        countula = countula + 1
    print('')
    cursor.close()
    db.close()
