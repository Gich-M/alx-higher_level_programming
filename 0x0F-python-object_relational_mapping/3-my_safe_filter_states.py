#!/usr/bin/python3
"""Takes in an argument and displays all values in the states
            table of hbtn_0e_0_usa where name matches the argument.
            SQL injection safe"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    arg = sys.argv[4]
    curr.execute("SELECT * FROM states WHERE name LIKE %s", (arg, ))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
