
import sqlite3
import webbrowser


def search():
    # database file connection
    database = sqlite3.connect("Database")
    # cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers
    cursor = database.cursor()

    temp =  input("Do you understand how to search(y/n)?\n")
    if temp =="y" or "Y":
        tempSearch = input("Enter a mySQL query :\n")
        cursor.execute(tempSearch)
        searchResult = cursor.fetchall()
        for x in searchResult:
            print(x)
    elif temp =="n" or "N":
        webbrowser.open('https://www.digitalocean.com/community/tutorials/introduction-to-queries-mysql')
    else:
        pass

    database.close()

