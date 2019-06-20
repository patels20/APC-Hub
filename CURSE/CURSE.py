# Ameer Noufal / Dan Smith de Paz
# APC - Assignment 4
from enum import Enum

class System_state(Enum):  # datatype created to keep track of what state the program is in
    log_on = 1
    run_student = 2  # there will be more of these
    error = 3


class User:
    # Base Class that all classes are built off of
    def __init__(self, user_id="", first_name="", last_name="", passcode=""):
        # This is the initialization function
        # if no paramaters are passed into it, the default listed will be used

        self.user_id = user_id          # User ID - It must be UNIQUE
        self.first_name  = first_name   # User's First Name
        self.last_name = last_name      # User's Last Name
        self.passcode = passcode        # Passcode is used for initial Login

#create an inherited class for the Professor:
class Faculty(User):
    def __init__(self):
        User.__init__(self,user_id="prof",first_name="Boring",last_name="idiot",passcode="hw")
        # initialize the user parts of the Professor class

        self.crns = []                     #list the CRN's that the Professor is teaching

#Create an inherited class for the Student:
class Student(User):
    def __init__(self, major="CM"):
        User.__init__(self, user_id="123", first_name="Ben", last_name="Dover", passcode="321")
        # initialize the user parts of the student class

        self.major = major              # So What's Your Major?
        self.crns = []                  # List of courses that the student is registered in

def create_test_student(entire_userbase):   # Generates a single student and adds it to the database
    entire_userbase.append(Student())       # no input parameters to a new student means the default will be used

def create_test_professor(entire_userbase): #Generate a Professor to test and add it to the database
    entire_userbase.append(Faculty())       # no input parameters to a new Professor means the default will be used

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

def run_student(userbase, activeuser): # Student Functionality

    temp = input("\nWhich Option?\n0 - Logout\n1 - Something else maybe\n")

    if temp == "0":    # logs the student out
        print("\nYOU HAVE BEEN LOGGED OUT\n")
        activeuser.clear()  # clears the active user list
        return System_state.log_on  # back to the logon
    elif temp == "1":   # this isn't anything right now just a place holder
        print("\nYou Fool, You fell for one of the classic blunders!\n")
        return System_state.run_student

def main():  # The logic of the program will happen in here to make sure nearly everything is defined in a method
    current_state = System_state(1)     # The Initialized state of the program is log_on to run that specific functionality
    test_database = []                  # hopefully this gets replaced with some sort of actual database system
    create_test_student(test_database)  # Adds a student to the "database"

    active_user = []                    # this is a temporary workaround until someone thinks of a better way to pass data around
                                        # This user's data is saved for refrence
                                        # there should never be more than 1 item in this list

    while 1:                            # infinite loop to run infinitely
        if current_state == System_state.log_on:   # switch-case depending on the state of the program
            current_state = log_on( test_database, active_user)  # the function returns the new state of the system
        elif current_state == System_state.error:                # if there's an error the program ends to let you know there's some flawed code
            exit("There was an error")
        elif current_state == System_state.run_student:          # This if will execute the functionality of the student
            current_state = run_student(test_database, active_user)

main()  # Hopefully the only function that is run globally


# end of file
