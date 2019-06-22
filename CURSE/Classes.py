from enum import Enum


class System_state(Enum):  # datatype created to keep track of what state the program is in
    log_on = 1
    run_student = 2  # there will be more of these
    error = 3
    run_admin = 4
    run_proffesor = 5


class User:
    # Base Class that all classes are built off of
    def __init__(self, user_id="", first_name="", last_name="", passcode=""):
        # This is the initialization function
        # if no paramaters are passed into it, the default listed will be used

        self.user_id = user_id  # User ID - It must be UNIQUE
        self.first_name = first_name  # User's First Name
        self.last_name = last_name  # User's Last Name
        self.passcode = passcode  # Passcode is used for initial Login


class Student(User):
    def __init__(self, major="CM"):
        User.__init__(self, user_id="", first_name="Ben", last_name="Dover", passcode="")
        # initialize the user parts of the student class

        self.major = major  # So What's Your Major?
        self.crns = []  # List of courses that the student is registered in

    def add_course(self, crn_code):
        self.crns.append(crn_code)

    def view_schedule(self, coursebase):
        for crn in self.crns:
            for course in coursebase:
                if crn == course.crn:
                    course.print_course()
                    break


class Proffesor(User):
    def __init__(self, crn="33"):
        User.__init__(self, user_id="a", first_name="yeet", last_name="teey", passcode="a")
        self.crns = []
        self.crns.append(crn)

    def view_rosters(self, coursebase, userbase):
        for crn in self.crns:
            for course in coursebase:
                if crn == course.crn:
                    course.print_course()
                    course.print_roster()
                    break


# Create an inherited class for the admin:
class Admin(User):
    def __init__(self, crn="33"):
        User.__init__(self, user_id="admin", first_name="Grande", last_name="Barriga", passcode="admin1")
        self.crns = []
        self.crns.append(crn)

    def view_rosters(self, coursebase, userbase):
        for crn in self.crns:
            for course in coursebase:
                if crn == course.crn:
                    course.print_course()
                    course.print_roster()
                    break


class Course():
    def __init__(self, crn="33", name="Binary for Bozos", instructor="THIS NEEDS TO BE A USER", length_course=1,
                 max_size=2, major="cs"):
        self.crn = crn  # Unique identifier
        self.name = name  # Name of the course
        self.instructor = instructor  # Name of the Teacher user that teaches
        self.roster = []  # List of Student Users Currently registered
        self.max_size = max_size  # Size limit of the the course
        self.major = major

        self.length_course = length_course  # the actual length of the course
        self.times = []  # The Index values correspond with each other
        self.days = []  #

    def add_student(self, student):
        if len(self.roster) >= self.max_size:  # Checks for course capacity
            print("ERROR COURSE AT CAPACITY")
            return 0  # Wait untill implemented
        else:
            self.roster.append(student)  # if there's no conflicts add the student to the roster
            return 1

    def print_course(self):
        print(
                    "\nCrn code: " + self.crn + "   Course: " + self.name + "   Instructor: " + self.instructor + "   Major: " + self.major + " Capacity: " + str(
                self.max_size) + " Open Seats: " + str(self.max_size - len(self.roster)))

    def print_roster(self):
        for x in self.roster:
            print(x.first_name)
