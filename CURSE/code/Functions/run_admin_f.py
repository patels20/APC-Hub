from Functions.logout_f import logout
from Classes.states import System_state
from Functions.create_course_f import create_course
from Functions.delete_course_f import delete_course
from Functions.print_courses_f import print_courses


def run_admin(coursebase, userbase, activeuser):
    temp = input("\nWhich Option?\n0 - Logout\n1 - Add a course\n2 - Delete a course\n3 - View Coursebase\n")
    if temp == "0":  # logs the user out
        return logout(activeuser)
    elif temp == "1":
        create_course(coursebase, userbase, activeuser)

    elif temp == "2":
        delete_course(userbase, coursebase)
    elif temp == "3":
        print_courses(coursebase)
    else:
        print("\n INVALID INPUT\n")
    return System_state.run_admin
