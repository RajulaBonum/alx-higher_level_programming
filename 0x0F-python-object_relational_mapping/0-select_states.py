#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    #connecting to MySQL server
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    #creating a cursor object to execute queries
    cur = conn.cursor()
    #Execute the query to select all states and order by id
    cur.execute("SELECT * FROM states")
    #Fetch all rows and display the results
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    #close the cursor and the database connection
    cur.close()
    conn.close()
