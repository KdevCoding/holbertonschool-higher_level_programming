import MySQLdb
import sys

if __name__ == "__main__":
    """querry of states
    """
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=password, db=database , charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT state FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
    pass