#!/usr/bin/python3
"""querry of states
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
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print("{}".format(row))
    cur.close()
    conn.close()
