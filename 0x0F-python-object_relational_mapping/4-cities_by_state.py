#!/usr/bin/env python3
"""Lists all cities from the database hbtn_0e_4_usa."""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
            INNER JOIN states ON states.id=cities.states_id
            ORDER BY cities.id ASC""")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
