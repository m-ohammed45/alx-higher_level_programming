#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3],port3306)
    c = db.cursor()
    c.excute("SELECT * FORM states")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()

