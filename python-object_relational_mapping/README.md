Python - Object-relational mapping

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why Python programming is awesome
How to connect to a MySQL database from a Python script
How to SELECT rows in a MySQL table from a Python script
How to INSERT rows in a MySQL table from a Python script
What ORM means
How to map a Python Class to a MySQL table

Tasks
0. Get all states
Write a script that lists all states from the database hbtn_0e_0_usa:
-	Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
-	You must use the module MySQLdb (import MySQLdb)
-	Your script should connect to a MySQL server running on localhost at port 3306
-	Results must be sorted in ascending order by states.id
-	Results must be displayed as they are in the example below
-	Your code should not be executed when imported