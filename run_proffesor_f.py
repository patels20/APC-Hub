from Functions.logout_f import logout
from Classes.states import System_state


def run_proffesor(coursebase, userbase, activeuser):
    temp = input("\nWhich Option?\n0 - Logout\n1 - View Class rosters \n")
    if temp == "0":  # logs the user out
        return logout(activeuser)
    elif temp == "1":
        activeuser[0].view_rosters(coursebase,userbase)
        return System_state.run_proffesor
    else:
        print("\n INVALID INPUT\n")
        return System_state.run_proffesor


