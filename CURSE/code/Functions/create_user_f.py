from Classes.student_c import Student
from Classes.proffesor_c import Proffesor
from Classes.user_c import User

from Classes.course_c import Course


def create_user():  # This function
    use_id = input("\nEnter User ID: \n")
    use_passcode = input("\nEnter User Pass code: \n")
    use_firstname = input("\nEnter User's First Name: \n")
    use_lastname = input("\nEnter User's Last Name: \n")
    temp = User(use_id, use_firstname, use_lastname, use_passcode)
    return temp


def create_student(entire_userbase):
    new_student = create_user()
    new_student.__class__ = Student
    new_student.major = input("\nInput the Student's major: \n")
    entire_userbase.append(new_student)  # adds the user to the userbase after the student is created


def create_proffesor(entire_userbase):
    new_proffesor = create_user()
    new_proffesor.__class__ = Proffesor
    # new_proffesor.crn.clear()
    entire_userbase.append(new_proffesor)  # adds the professor to the userbase after they are created
