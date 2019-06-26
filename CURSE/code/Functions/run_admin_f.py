from Functions.logout_f import logout
from Classes.states import System_state
from Functions.create_course_f import create_course

def run_admin(coursebase, userbase, activeuser):
    temp = input("\nWhich Option?\n0 - Logout\n1 - Add a course\n")
    if temp == "0":  # logs the user out
        return logout(activeuser)
    elif temp == "1":
        create_course(coursebase, userbase, activeuser)
        return System_state.run_admin
    else:
        print("\n INVALID INPUT\n")
        return System_state.run_admin
