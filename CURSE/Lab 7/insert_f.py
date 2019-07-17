import sqlite3

#this function allows the user to insert anything into the appropriate database

def insert():

    # database file connection
    database = sqlite3.connect("Database")
    # cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers
    cursor = database.cursor()

    temp = input("\nWhat would you like to insert?\n0 - nothing\n1 - Student\n")
    if temp == "1": # student
        # INSERT INTO STUDENT VALUES(00010001, 'Isaac', 'Newton', 1668, 'BSAS', 'newtoni')
        ID = input("Enter User ID: \n")
        NAME = input("Enter Name: \n")
        SURNAME = input("Enter Surname: \n")
        YEAR = input("Enter graduation year: \n")
        MAJOR = input("Enter major in all caps: \n")
        EMAIL = input("Enter email: \n")

        cursor.execute( "INSERT INTO STUDENT VALUES(?, ?, ?, ?, ?, ?); ", (ID, NAME, SURNAME, int(YEAR), MAJOR,EMAIL) )

        # cursor.execute("""SELECT * FROM STUDENT""")
        # query_result = cursor.fetchall()
        #
        # for i in query_result:
        #     print(i)

    # elif temp == "2": # instructor
    #     pass
    # elif temp == "3": # course
    #     pass
    # elif temp == "4": # admin
    #     pass
    elif temp == "0": # quit
        pass
    else:
        print("incorrect output")

    # To save the changes in the files. Never skip this.
    # If we skip this, nothing will be saved in the database.
    database.commit()
    database.close()

