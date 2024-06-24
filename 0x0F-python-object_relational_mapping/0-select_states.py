#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

if __name__ == "__main__":

   mydb = MySQLdb.connect(host="localhost", user=sys.argv[1],
           psswd=sys.argv[2],db=sys.argv[3],port=3306)
    cur= mydb.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    mydb.close()

