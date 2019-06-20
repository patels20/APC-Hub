# Ameer Noufal / Dan Smith de Paz
# APC - Assignment 4

from Classes import*


def create_test_student(entire_userbase):   # Generates a single student and adds it to the database
    entire_userbase.append(Student())       # no input parameters to a new student means the default will be used


def create_test_course(entire_classbase):
    entire_classbase.append(Course())


def create_initial_admin(entire_userbase):  # Generate a admin to be logged onto so that they may add other students
    # and faculty
    entire_userbase.append(Admin())  # no input parameters to a new admin means that the default is used.




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
            # ADD CASES FOR OTHER USER TYPES

            return System_state.error # something's wrong if this happens

    print(" INCORRECT USERNAME OR PASSCODE\n")  # Tell's the user they Goofed
    activeuser.clear() # just to make sure that there's no active user if the logon failed
    return System_state.log_on  #


def register_course(coursebase,activeuser):
    #  This function has the user input a CRN-
    #  code and attempts to register for it

    temp = input("Input the crn value of the course you want to register")
    for course in coursebase:
        if temp == course.crn:                      # if the course exists attempt to register the active user
            course.add_student(activeuser[0])
            print("\nsuccessfuly registered for:" + temp + "\n")
            return
    print("\nFailed to register\n")
    return


def run_student(coursebase, activeuser): # Student Functionality

    temp = input("\nWhich Option?\n0 - Logout\n1 - Add a course\n")

    if temp == "0":    # logs the student out
        print("\nYOU HAVE BEEN LOGGED OUT\n")
        activeuser.clear()  # clears the active user list
        return System_state.log_on  # back to the logon
    elif temp == "1":   # this is the register for a class functionality

        register_course(coursebase, activeuser) # Attempt to register for a class
        return System_state.run_student




def main():  # The logic of the program will happen in here to make sure nearly everything is defined in a method
    current_state = System_state(1)     # The Initialized state of the program is log_on to run that specific functionality

    test_userbase = []                  # hopefully this gets replaced with some sort of actual database system
    create_test_student(test_userbase)  # Adds a student to the "database"
    create_initial_admin(test_userbase)  # Adds an admin from the "database"

    test_coursebase = []                # Temporary class database
    create_test_course(test_coursebase) # Adds a class to the "database"



    active_user = []                    # this is a temporary workaround until someone thinks of a better way to pass data around
                                        # This user's data is saved for refrence
                                        # there should never be more than 1 item in this list

    while 1:                            # infinite loop to run infinitely
        if current_state == System_state.log_on:   # switch-case depending on the state of the program
            current_state = log_on( test_userbase, active_user)  # the function returns the new state of the system
        elif current_state == System_state.error:                # if there's an error the program ends to let you know there's some flawed code
            exit("There was an error")
        elif current_state == System_state.run_student:          # This if will execute the functionality of the student
            current_state = run_student(test_coursebase, active_user)

main()  # Hopefully the only function that is run globally


# end of file
