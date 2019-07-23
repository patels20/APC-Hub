import sqlite3

#this function allows the user to insert anything into the appropriate database

def insert():

    # database file connection
    database = sqlite3.connect("Database")
    # cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers
    cursor = database.cursor()

    temp = input("\nWhat would you like to insert?\n0 - nothing\n1 - Student\n2 - Instructor\n3 - Admin")
    if temp == "1": # student
        # INSERT INTO STUDENT VALUES(00010001, 'Isaac', 'Newton', 1668, 'BSAS', 'newtoni') --example
        ID = input("Enter User ID: \n")
        NAME = input("Enter Name: \n")
        SURNAME = input("Enter Surname: \n")
        YEAR = input("Enter graduation year: \n")
        MAJOR = input("Enter major in all caps: \n")
        EMAIL = input("Enter email: \n")

        cursor.execute( "INSERT INTO STUDENT VALUES(?, ?, ?, ?, ?, ?); ", (ID, NAME, SURNAME, int(YEAR), MAJOR,EMAIL) )

        #cursor.execute("""SELECT * FROM STUDENT""")
        #query_result = cursor.fetchall()
        #
        #for i in query_result:
        #     print(i)

    elif temp == "2": # instructor
             #INSERT INTO INSTRUCTOR VALUES(00020001, 'Joseph', 'Fourier', 'Full Prof.', 1820, 'BSEE', 'fourierj') --example
        ID = input("Enter the User ID: \n")
        NAME = input("Enter Name: \n")
        SURNAME = input("Enter Surname: \n")
        TITLE = input("Enter Title: \n")
        HIREYEAR = input("Enter the year they were hired: \n")
        DEPT = input("Enter their Department: \n")
        EMAIL = input("Enter their email: \n")

        cursor.execute( "INSERT INTO INSTRUCTOR VALUES(?, ?, ?, ?, ?, ?, ?); ", (ID, NAME, SURNAME, TITLE, int(HIREYEAR), DEPT, EMAIL) )

        #cursor.execute("""SELECT * FROM INSTRUCTOR""")
        #query_result = cursor.fetchall()
        #for i in query_result:
        #    print(i)

    elif temp == "3": # course
        CRN = input("what is the course CRN?: \n")
        NAME = input("What is the course name?: \n")
        ROSTER = input("are students being signed up?") # this is just a filler until a course can be made.

        cursor.execute("INSERT INTO INSTRUCTOR VALUES(?, ?, ?); ",(CRN, NAME, ROSTER))

        # cursor.execute("""SELECT * FROM COURSE""")
        # query_result = cursor.fetchall()
        #for i in query_result:
            #print(i)

    elif temp == "4": # admin
        ID = input("Enter the new admin's ID: \n")
        NAME = input("Enter their name: \n")
        SURNAME = input("Enter their Surname: \n")
        TITLE =  input("enter their title: \n")
        OFFICE =  input("where is their office? \n")
        EMAIL = input("what is their email? \n")

        cursor.execute("INSERT INTO ADMIN VALUES(?, ?, ?, ?, ?, ?);", (ID,NAME,SURNAME,TITLE,OFFICE,EMAIL))
    

    elif temp == "0": # quit
        pass
    else:
        print("incorrect output")

    # To save the changes in the files. Never skip this.
    # If we skip this, nothing will be saved in the database.
    database.commit()
    database.close()

