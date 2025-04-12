#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
Usage: ./0-select_states.py <mysql_username> <mysql_password> <database_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )

    # Create a cursor and execute the query
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print all results
    for row in cur.fetchall():
        print(row)

    # Close the cursor and connection
    cur.close()
    db.close()
