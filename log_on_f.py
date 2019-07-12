from Classes.states import System_state
from Classes.student_c import Student
from Classes.proffesor_c import Proffesor
from Classes.admin_c import Admin



def log_on( userbase, activeuser):
    temp = input("\nENTER USERNAME:\n")    # take in user log on info
    orary = input("\nENTER PASSCODE:\n")     #

    for dude in userbase:                   # Increment's through the list of people in the database
        if temp == dude.user_id and orary == dude.passcode:  # If the credentials match!
            # save the user info to the list
            activeuser.clear()          # clear the list to make sure it's empty before adding
            activeuser.append(dude)     # add the user to the list for future reference
            # This if block changes the state of the program depending on what class the user is
            if dude.__class__ == Student:
                print("\n Welcome " + activeuser[0].first_name) # greets the user
                return System_state.run_student # returns the new state of the program
            if dude.__class__ == Admin:
                print("\n Administrator : " + activeuser[0].first_name + " " + activeuser[0].last_name + " has logged on\n")
                return System_state.run_admin
            if dude.__class__ == Proffesor:
                print("\n Welcome " + activeuser[0].first_name)
                return System_state.run_proffesor

            return System_state.error # something's wrong if this happens

    print(" INCORRECT USERNAME OR PASSCODE\n")  # Tell's the user they Goofed
    activeuser.clear() # just to make sure that there's no active user if the logon failed
    return System_state.log_on  #
