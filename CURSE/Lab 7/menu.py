from print_all_f import print_all
from search_f import search
from insert_f import insert


def menu():
    temp = input("\nWhich Option?\n0 - END PROGRAM\n1 - SEARCH BY DEPARTMENT\n2 - PRINT ALL\n3 - INSERT INTO A DATABASE\n")
    if temp == "0":  # ends program
        exit("PROGRAM TERMINATED:\nNO ERROR")
    elif temp == "1":  # search for something
        search()
    elif temp == "2":  # Print everything
       print_all()
    elif temp == "3":  # insert a student
        insert()
    else:
        print("\n INVALID INPUT\n")

    menu()
