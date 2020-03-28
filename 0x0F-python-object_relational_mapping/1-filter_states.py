#!/usr/bin/python3
import MySQLdb
from sys import argv


if __name__ == "__main__":

        db = MySQLdb.connect(host='localhost', user=argv[1],
                             passwd=argv[2], db=argv[3], port=3306)

        cur = db.cursor()

        cur.execute("SELECT id, name FROM states WHERE name RLIKE '^N|^n'\
        ORDER BY id ASC;")

        for QueryResult in cur:
            print(QueryResult)

        cur.close()
        db.close()
