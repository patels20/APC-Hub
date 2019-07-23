import sqlite3

# database file connection
database = sqlite3.connect("Database")

# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers
cursor = database.cursor()

def delete_instructor():
    targetCRN = input("please enter the ID of the instructor you want to delete")
    cursor.execute("DELETE FROM INSTRUCTOR WHERE ID = (?);", (targetCRN))
