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
        "SELECT cities.name FROM cities "
        "Left Join states ON cities.state_id = states.id "
        "Where states.name = %s"
        "ORDER BY cities.id ASC ", (sys.argv[4],)
    )
    print(", ".join(row[0] for row in cur.fetchall()))
    cur.close()
    conn.close()
