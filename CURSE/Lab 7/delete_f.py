import sqlite3

#this function allows the user to delete an instructor from the database

def delete_instructor():
    targetCRN = input("please enter the ID of the instructor you want to delete")
    cursor.execute("DELETE FROM INSTRUCTOR WHERE ID = (?);", (targetCRN))
