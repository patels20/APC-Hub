from Classes.states import System_state
from Functions.logout_f import logout
from Functions.register_course_f import register_course


def run_student(coursebase, userbase, activeuser):  # Student Functionality
    temp = input("\nWhich Option?\n0 - Logout\n1 - Register for a course\n2 - View schedule\n")
    if temp == "0":    # logs the student out
        return logout(activeuser) #this function returns the proper state meaning the value it returns will be returned
    elif temp == "1":   # this is the register for a class functionality

        register_course(coursebase, userbase, activeuser) # Attempt to register for a class then keep the user logged on
        return System_state.run_student
    elif temp == "2":
        activeuser[0].view_schedule(coursebase)
        return System_state.run_student
    else:
        print("\n INVALID INPUT\n")
        return System_state.run_student