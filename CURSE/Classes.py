
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
        self.first_name = first_name   # User's First Name
        self.last_name = last_name      # User's Last Name
        self.passcode = passcode        # Passcode is used for initial Login


class Student(User):
    def __init__(self, major="CM"):
        User.__init__(self, user_id="123", first_name="Ben", last_name="Dover", passcode="321")
        # initialize the user parts of the student class

        self.major = major              # So What's Your Major?
        self.crns = []                  # List of courses that the student is registered in


class Course():
    def __init__(self, crn="33", name="Binary for Bozos", instructor="THIS NEEDS TO BE A USER", length_course=1, max_size=2 ):
        self.crn = crn                  # Unique identifier
        self.name = name                # Name of the course
        self.instructor = instructor    # Name of the Teacher user that teaches
        self.roster = []                # List of Student Users Currently registered
        self.max_size = max_size        # Size limit of the the course

        self.length_course = length_course     # the actual length of the course
        self.times = []                 # The Index values correspond with each other
        self.days = []                  #
    def add_student(self, student):
        if len(self.roster) >= self.max_size:  # Checks for course capacity
            print("ERROR COURSE AT CAPACITY")
            #return System_state.error            # Wait untill implemented
        else:
            self.roster.append(student)         # if there's no conflicts add the student to the roster




