#!/usr/bin/python3
""" List all states with a name starting with N from database """
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[
        1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    cur.execute("""
            SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id
            """)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
