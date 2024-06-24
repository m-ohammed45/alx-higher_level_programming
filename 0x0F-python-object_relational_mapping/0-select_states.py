#!/usr/bin/python3
"""
Script that connects to a MySQL database and prints all states sorted by id.

Usage:
    ./0-select_states.py <username> <password> <database>
"""

import MySQLdb
import sys

def list_states(username, password, db_name):
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        states = cursor.fetchall()
        for state in states:
            print(state)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python list_states.py <username> <password> <db_name>")
        sys.exit(1)
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, db_name)

