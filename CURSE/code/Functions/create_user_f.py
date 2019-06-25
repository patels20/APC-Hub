from Classes.student_c import Student
from Classes.proffesor_c import Proffesor
from Classes.admin_c import Admin
from Classes.user_c import User

from Classes.course_c import Course


def create_user():  # This function
    use_id = input("\nEnter User ID: \n")
    use_passcode = input("\nEnter User Pass code: \n")
    use_firstname = input("\nEnter User's First Name: \n")
    use_lastname = input("\nEnter User's Last Name: \n")
    temp = User(use_id, use_firstname, use_lastname, use_passcode)
    return temp


def create_student():
    new_student = create_user()
    new_student.__class__ = Student
    new_student.major = input("\nInput the Student's major: \n")

def create_proffesor():
    new_proffesor = create_user()
    new_proffesor.__class__ = Proffesor



