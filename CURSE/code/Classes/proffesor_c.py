from Classes.user_c import *
class Proffesor(User):
    def __init__(self, crn="33"):
        User.__init__(self, user_id = "a", first_name = "ye",last_name = "et", passcode = "a")
        self.crns = []
        # crn = 33 is unused at the moment
    def view_rosters(self,coursebase, userbase):
        for crn in self.crns:
            for course in coursebase:
                if crn == course.crn:
                    course.print_course()
                    course.print_roster()
                    break