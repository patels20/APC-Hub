from Classes.states import System_state


def logout(activeuser):                 # this method is called when the program needs to return to the login state
    print("\n" + activeuser[0].first_name +" HAS BEEN LOGGED OUT\n")
    activeuser.clear()  # clears the active user list
    return System_state.log_on  # back to the logon
