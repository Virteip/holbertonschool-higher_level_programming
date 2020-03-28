#!/usr/bin/python3
import MySQLdb
from sys import argv


if len(argv) - 1 == 4:

    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)

    cur = db.cursor()

    query_line = "SELECT id, name FROM states WHERE name\
    LIKE %s ORDER BY id ASC;"

    cur.execute(query_line, (argv[4], ))

    for result in cur:
        print(result)
else:
    pass
