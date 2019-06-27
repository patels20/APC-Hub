from Functions.log_on_f import log_on
from Classes.student_c import *


class Course():
    def __init__(self, crn="33", name="Binary for Bozos", instructor="THIS NEEDS TO BE A USER", length_course=1, max_size=2, major = "cs",
                 grade = "junior"):
        self.crn = crn                  # Unique identifier
        self.name = name                # Name of the course
        self.instructor = instructor    # Name of the Teacher user that teaches
        self.roster = []                # List of Student Users Currently registered
        self.max_size = max_size        # Size limit of the the course
        self.major = major

        self.grade_level = grade        # Educational level required in order to sign up
        self.restrictions = []          # Set of prerequsites if any exists
        self.subjects = []              # Course categories


        self.length_course = length_course     # the actual length of the course
        self.times = []                 # The Index values correspond with each other
        self.days = []                  #


    def add_student(self, student):
        print(student.grade)
        for x in student.crns[0][student.grade]:
            for z in student.crns:
                if (student.crn == student.crns[x, z]):    #Checks previous years for completed prerequsites
                    return 1
                else:
                    return 0
        if len(self.roster) >= self.max_size:  # Checks for course capacity
            print("ERROR COURSE AT CAPACITY")
            return 0            # Wait untill implemented
        else:
            self.roster.append(student)         # if there's no conflicts add the student to the roster
            return 1
    def print_course(self):
        print("\nCrn code: " + self.crn + "   Course: " + self.name + "   Instructor: " + self.instructor + "   Major: " + self.major + " Capacity: " + str(self.max_size)  + " Open Seats: " + str(self.max_size - len(self.roster)))
    def print_roster(self):
        for x in self.roster:
            print(x.first_name)


