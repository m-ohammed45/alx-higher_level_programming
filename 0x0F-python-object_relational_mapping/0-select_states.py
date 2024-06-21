#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0usa"""

import MySQLdb

def get_states(username, password, database):
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database)

        # Create a cursor object
        cursor = db.cursor()

        # Execute the query to retrieve states
        cursor.execute("SELECT id, name FROM states ORDER BY id")

        # Fetch all rows
        rows = cursor.fetchall()

        # Print the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the database connection
        db.close()

if __name__ == "__main__":
    username = "root"
    password = "root"
    database = "hbtn_0e_0_usa"

    get_states(username, password, database)


