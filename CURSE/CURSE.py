# Ameer Noufal / Dan Smith de Paz
# APC - Assignment 4


class User:
    # Base Class that all classes are built off of
    def __init__(self, user_id="heisenberg", first_name="Walter", last_name="White", passcode="meth"):
        # This is the initialization function
        # if no paramaters are passed into it, the default listed will be used

        self.user_id = user_id          # User ID - It must be UNIQUE
        self.first_name  = first_name   # User's First Name
        self.last_name = last_name      # User's Last Name
        self.passcode = passcode        # Passcode is used for initial Login


class Student(User):
    def __init__(self, major="Chem"):
        User.__init__(self, user_id="heisenberg", first_name="Walter", last_name="White", passcode="meth")
        # initialize the user parts of the student class

        self.major = major              # So What's Your Major?
        self.crns = []                  # List of courses that the student is registered in


def create_test_student(entire_userbase):   # Generates a single student and adds it to the database
    entire_userbase.append(Student())       # no input parameters to a new student means the default will be used


def main():  # The logic of the program will happen in here to make sure nearly everything is defined in a method

    test_database = []                  # hopefully this gets replaced with some sort of actual database system
    create_test_student(test_database)  # Adds a student to the "database"
    print(test_database[0].first_name)  # verifies the student exists


main()  # Hopefully the only function that is run globally


# end of file
