#!/usr/bin/python3
"""
pass name to look for in argv
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)

    cur = db.cursor()

    cur.execute("SELECT id, name FROM states WHERE name LIKE BINARY '{:s}'\
    ORDER BY id ASC;".format(argv[4]))

    for result in cur:
        print(result)
