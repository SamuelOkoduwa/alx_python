#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main":
    # Get the MySQL username, password, and database name from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server running on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query to fetch all states and sort by states.id
    cur.execute("SELECT * FROM states ORDER BY states.id")

    # Fetch and display the results
    results = cur.fetchall()
    for row in results:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
