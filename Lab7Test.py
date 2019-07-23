"\n1 - Simple(1 Table with 1 specific criteria)"
"\n2 - Intermediate(2 Table with a 2 specific criteria)"
"\n3 - Advanced (All available Tables with 3 specific criteria)\n")
if tempSearch == "1":
    TABLE = input("What table do you want to search\n1 - Student \n2 - Instructor \n3 - Admin\n")
if TABLE == "1":
    A, B, C, D, E, F = input("What field(s) do you want to search?(6 Inputs, Space = no more)\n1 - ID\n2 - Name"
"\n3 - Surname\n4 - GradYear\n5 - Major\n6 - Email\n")
cursor.execute("SELECT (?, ?, ?, ?, ?, ?) FROM STUDENT;", (A, B, C, D, E, F))

# cursor.execute( "INSERT INTO STUDENT VALUES(?, ?, ?, ?, ?, ?); ", (ID, NAME, SURNAME, int(YEAR), MAJOR,EMAIL) )

# "SELECT personal || ' ' || family FROM Person WHERE id='" + person_id + "';"


import sqlite3
import webbrowser


def search():
    # database file connection
    database = sqlite3.connect("Database")
    # cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers
    cursor = database.cursor()

    temp =  input("Do you understand how to search(y/n)?\n")
    if temp =="y" or "Y":
        tempSearch = "SELECT personal || ' ' || family FROM Person WHERE id=?;"
        cursor.execute("SELECT NAME FROM STUDENT")
        searchResult = cursor.fetchall()
        for x in searchResult:
            print(x)
    elif temp =="n" or "N":
        webbrowser.open('https://www.digitalocean.com/community/tutorials/introduction-to-queries-mysql')
    else :
        print("Invalid Option")


    database.close()

