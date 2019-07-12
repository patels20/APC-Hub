from Functions.logout_f import logout
from Classes.states import System_state
from Functions.create_course_f import create_course
from Functions.delete_course_f import delete_course
from Functions.print_courses_f import print_courses
from Functions.create_user_f import *


def run_admin(coursebase, userbase, activeuser):
    temp = input("\nWhich Option?\n0 - Logout\n1 - Add a course\n2 - Delete a course\n3 - View Coursebase\n4 - create student\n5 - create Professor\n")
    if temp == "0":  # logs the user out
        return logout(activeuser)
    elif temp == "1":
        create_course(coursebase, userbase, activeuser)
    elif temp == "2":
        delete_course(userbase, coursebase)
    elif temp == "3":
        print_courses(coursebase)
    elif temp =="4":
        create_student(userbase)
    elif temp =="5":
        create_proffesor(userbase)
    else:
        print("\n INVALID INPUT\n")
    return System_state.run_admin
