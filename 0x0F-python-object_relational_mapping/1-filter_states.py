#!/usr/bin/python3
"""Lists all states with a name starting with N (upper N)
            from the database hbtn_0e_0_usa."""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE
                        name LIKE BINARY 'N%' ORDER BY states.id ASC""")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
