#!/usr/bin/python3
import MySQLdb
from sys import argv


if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)

    cur = db.cursor()

    query_line = "SELECT cities.name FROM cities\
    JOIN states ON states.id = cities.state_id\
    WHERE states.name = %s\
    ORDER BY cities.id ASC;"

    cur.execute(query_line, (argv[4], ))

    query = cur.fetchall()
    list = []
    for result in query:
        list.append(result[0])

    print(', '.join(list))
