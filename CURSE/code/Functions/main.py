from Functions.create_test_users_f import *
from Classes.states import System_state
from Functions.log_on_f import log_on
from Functions.run_student_f import run_student
from Functions.run_admin_f import run_admin
from Functions.run_proffesor_f import run_proffesor
from Classes.semester_c import *

def main():  # The logic of the program will happen in here to make sure nearly everything is defined in a method
    current_state = System_state(1)     # The Initialized state of the program is log_on to run that specific functionality

    semester = []
    semester.append(Semester(2000,"fall"))
    semester.append(Semester(2001, "spring"))
    test_userbase = [Student("29412","Ameer","Noufal","iHatecats","Computer Engineering",3),
                     Student("17412","Shail","Patel","Hobart","Electrical Engineering",3),
                     Student("75125","Dan","Smith-De Paz","iLovedogs","Biomedical Engineering",3),
                     Student("61241","Chandler","Bing","monica","Comedian Engineering",1),
                     Student("23429","Scooby","Doo","monsterinc","Civil Engineering",4),
                     Student("91284","Tom","Brady","hateFutball","Sports Marketing Engineering",4),
                     Student("28352","Donald","Obama","2020","Political Engineering",2),
                     Student("84242","Joe","Sanders","3030","Computer Engineering",2),
                     Student("42099","Area","Fifty-One","5151","Electrical and Computer Engineering",2),
                     Student("89123","Sheep","Goat","baaaa","Mechanical Engineering",1)]                  # hopefully this gets replaced with some sort of actual database system
  
    create_test_student(test_userbase)  # Adds a student to the "database"
    create_initial_admin(test_userbase)  # Adds an admin from the "database"
    create_test_teacher(test_userbase)

    test_coursebase = [Course("12345", "Computer Architect", "Marisha Rawlins", 3, 8, "Electrical Engineering", 3),
                       Course("3550", "Computer Networks", "Wayne Bynoe", 3, 8, "Computer Engineering", 3),
                       Course("3600", "Signal and Systems", "Saurav Basnet", 4, 8, "Computer and Electrical Engineering", 3),
                       Course("3225", "Applied Programming Concepts", "Aaron Carpenter", 5, 8, "Copmuter and Electrical Engineering", 3),
                       Course("4829", "Junior Design", "The Trifecta", 10, 8, "Anything Engineering", 3)]                # Class database
    create_test_course(test_coursebase) # Adds a class to the "database"

    active_user = []                    # this is a temporary workaround until someone thinks of a better way to pass data around
    active_semester = []                                   # This user's data is saved for refrence
                                        # there should never be more than 1 item in this list



    while 1:                            # infinite loop to run infinitely

        if current_state == System_state.log_on:   # switch-case depending on the state of the program
            current_state = log_on(test_userbase, active_user, semester, active_semester)  # the function returns the new state of the system
        elif current_state == System_state.error:                # if there's an error the program ends to let you know there's some flawed code
            exit("There was an error")
        elif current_state == System_state.run_student:          # This if will execute the functionality of the student
            current_state = run_student(test_coursebase, test_userbase, active_user)
        elif current_state == System_state.run_admin:
            current_state = run_admin(test_coursebase, test_userbase, active_user)
        elif current_state == System_state.run_proffesor:
            current_state = run_proffesor(test_coursebase, test_userbase, active_user)

main()  # Hopefully the only function that is run globally
