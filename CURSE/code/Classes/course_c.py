from Functions.log_on_f import log_on
from Classes.student_c import *
from Classes.semester_c import *

class Course():
    def __init__(self, crn="", name="Binary for Bozos", instructor="THIS NEEDS TO BE A USER", length_course=1, max_size=2, major = "cs",
                 grade = 1, semester = Semester(1999,trimester.Fall)):
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
        self.semester = semester


    def add_student(self, student):        

        if len(self.roster) < self.max_size:  # Checks for course capacity
            if int(self.grade_level) <= int(student.grade): # checks for appropriate
                if len(self.restrictions) > 0 :
                    conflict = True

                    for rec in self.restrictions:
                        for course in student.crns:
                            # if the student has taken the prerec make conflict false and stop checking
                            if course == rec:
                                conflict = False
                                break

                        #  If the course is there
                        if conflict == False:
                            conflict = True
                            # if it's the last course in the prerec list
                            if rec == self.restrictions[len(self.restrictions)-1]:
                                self.roster.append(student)  # if there's no conflicts add the student to the roster
                                return 1

                        else:
                            print("\nYOU LACK THE NECESARY PRE-REQUIRMENTS\n")
                            break

                else:
                    # If there's no Restrictions
                    self.roster.append(student)
                    return 1

            else:
                print("\nYOU REQUIRE MORE XP FOR THIS QUEST\n")

        else: # this else block will check
            print("ERROR COURSE AT CAPACITY")
        return 0
        
    def print_course(self):
        print("\nCrn code: " + self.crn + "   Course: " + self.name + "   Instructor: " + self.instructor + "   Major: " + self.major + " Capacity: " + str(self.max_size)  + " Open Seats: " + str(self.max_size - len(self.roster)))
    def print_roster(self):
        for x in self.roster:
            print(x.first_name)


