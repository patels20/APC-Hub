from Classes.user_c import *
class Student(User):
    def __init__(self, user_id="", first_name="Ben", last_name="Dover", passcode="",major="CM", grade=1):
        # initialize the user parts of the student class
        self.user_id = user_id;
        self.first_name = first_name;
        self.last_name = last_name
        self.passcode=passcode;
        self.major = major              # So What's Your Major?
        self.crns = []                  # List of courses that the student is registered in
        self.course_limit = 4           # Number of courses per semester
        self.grade = grade              # A students current grade level


    def add_course(self,crn_code):
        self.crns.append(crn_code)
    def view_schedule(self, coursebase):
        for crn in self.crns:
            for course in coursebase:
                if crn == course.crn:
                    course.print_course()
                    break
