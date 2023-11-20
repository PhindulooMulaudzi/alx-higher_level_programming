#!/usr/bin/python3
"""list states in database"""
from sys import argv
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306, host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY id ASC;')
    states = cursor.fetchall()
    for st in states:
        print(st)
