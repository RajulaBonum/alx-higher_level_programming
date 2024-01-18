#!/usr/bin/python3
"""This is a safe filter for a specific name in a db"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    match = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
