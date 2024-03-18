#!/usr/bin/env python3
"""Lists all cities from that state
    from the database hbtn_0e_4_usa."""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    cur.execute("""SELECT cities.name FROM cities
            INNER JOIN states ON states.id=cities.state_id
            WHERE states.name=%s ORDER BY cities.id ASC""", (sys.argv[4],))
    states = cur.fetchall()
    temp = list(state[0] for state in states)
    print(*temp, sep=", ")
    cur.close()
    conn.close()
