#!/usr/bin/python3
"""
select all cities from state
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
    LEFT JOIN states ON states.id = cities.state_id\
    ORDER BY cities.id ASC")

    query = cur.fetchall()

    for result in query:
        print(result)
