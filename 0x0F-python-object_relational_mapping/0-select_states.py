#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0usa"""

import MySQLdb

def get_states(username, password, database):
    try:
        db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database)

        cursor = db.cursor()

        cursor.execute("SELECT id, name FROM states ORDER BY id")

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        db.close()

if __name__ == "__main__":
    username = "root"
    password = "root"
    database = "hbtn_0e_0_usa"

    get_states(username, password, database)


