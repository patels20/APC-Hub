import sqlite3

#this function prints everything in the database

def print_all():
    # database file connection
    database = sqlite3.connect("Database")
    # cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers
    cursor = database.cursor()

    # QUERY FOR ALL
    print("ENTIRE DATA BASE\nSTUDENTS:")
    cursor.execute("""SELECT * FROM STUDENT""")
    query_result = cursor.fetchall()

    for i in query_result:
        print(i)

    # QUERY FOR ALL
    print("\nINSTRUCTORS:")
    cursor.execute("""SELECT * FROM INSTRUCTOR""")
    query_result = cursor.fetchall()

    for i in query_result:
        print(i)

    # QUERY FOR ALL
    print("\nADMIN:")
    cursor.execute("""SELECT * FROM ADMIN""")
    query_result = cursor.fetchall()

    for i in query_result:
        print(i)

    # close the connection
    database.close()


