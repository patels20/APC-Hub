from Classes.user_c import *
class Student(User):
    def __init__(self, major="CM"):
        User.__init__(self, user_id="", first_name="Ben", last_name="Dover", passcode="")
        # initialize the user parts of the student class

        self.major = major              # So What's Your Major?
        self.crns = []                  # List of courses that the student is registered in
    def add_course(self,crn_code):
        self.crns.append(crn_code)
    def view_schedule(self, coursebase):
        for crn in self.crns:
            for course in coursebase:
                if crn == course.crn:
                    course.print_course()
                    break
