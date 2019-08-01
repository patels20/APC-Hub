from Classes.student_c import *

def print_students(userbase):

    for x in userbase:
        if x.__class__ == Student:
            print("\nID: " + x.user_id + "     Name: " + x.first_name + " " + x.last_name)


