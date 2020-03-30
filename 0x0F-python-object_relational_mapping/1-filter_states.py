#!/usr/bin/python3
"""
Print names that start with n
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":

        db = MySQLdb.connect(host='localhost', user=argv[1],
                             passwd=argv[2], db=argv[3], port=3306)
        cur = db.cursor()
        cur.execute("SELECT id, name FROM states WHERE name RLIKE '^N'\
        ORDER BY id ASC;")
        query = cur.fetchall()
        for result in query:
            print(result)
