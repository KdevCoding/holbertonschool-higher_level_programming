#!/usr/bin/python3
"""state query filter by input sqlinjection protection l join cities
filter by state
"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states",
        "Left Join cities ON cities.state_id = states.id",
        "WHERE = BINARY = %s ",
        "ORDER BY cities.id ASC", (sys.argv[4],)
    )
    for row in cur.fetchall():
        print(row[0], sep=',',end='')
    cur.close()
    conn.close()
