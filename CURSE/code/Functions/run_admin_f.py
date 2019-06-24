from Functions.logout_f import logout
from Classes.states import System_state

def run_admin(coursebase, userbase, activeuser):
    temp = input("\nWhich Option?\n0 - Logout\n EE \n")
    if temp == "0":  # logs the user out
        return logout(activeuser)
    else:
        print("\n INVALID INPUT\n")
        return System_state.run_admin
