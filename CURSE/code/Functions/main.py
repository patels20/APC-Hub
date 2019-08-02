from Functions.create_test_users_f import *
from Classes.states import System_state
from Functions.log_on_f import log_on
from Functions.run_student_f import run_student
from Functions.run_admin_f import run_admin
from Functions.run_proffesor_f import run_proffesor


def main():  # The logic of the program will happen in here to make sure nearly everything is defined in a method
    current_state = System_state(1)     # The Initialized state of the program is log_on to run that specific functionality

    semester = []

    test_userbase = []                  # hopefully this gets replaced with some sort of actual database system
    create_test_student(test_userbase)  # Adds a student to the "database"
    create_initial_admin(test_userbase)  # Adds an admin from the "database"
    create_test_teacher(test_userbase)

    test_coursebase = []                # Temporary class database
    create_test_course(test_coursebase) # Adds a class to the "database"

    active_user = []                    # this is a temporary workaround until someone thinks of a better way to pass data around
                                        # This user's data is saved for refrence
                                        # there should never be more than 1 item in this list



    while 1:                            # infinite loop to run infinitely
        if current_state == System_state.log_on:   # switch-case depending on the state of the program
            current_state = log_on(test_userbase, active_user)  # the function returns the new state of the system
        elif current_state == System_state.error:                # if there's an error the program ends to let you know there's some flawed code
            exit("There was an error")
        elif current_state == System_state.run_student:          # This if will execute the functionality of the student
            current_state = run_student(test_coursebase, test_userbase, active_user)
        elif current_state == System_state.run_admin:
            current_state = run_admin(test_coursebase, test_userbase, active_user)
        elif current_state == System_state.run_proffesor:
            current_state = run_proffesor(test_coursebase, test_userbase, active_user)

main()  # Hopefully the only function that is run globally