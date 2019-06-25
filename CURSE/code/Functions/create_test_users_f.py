from Classes.student_c import Student
from Classes.proffesor_c import Proffesor
from Classes.admin_c import Admin

from Classes.course_c import Course





def create_test_student(entire_userbase):   # Generates a single student and adds it to the database
    entire_userbase.append(Student())       # no input parameters to a new student means the default will be used


def create_test_teacher(entire_userbase):
    entire_userbase.append(Proffesor())


def create_test_course(entire_classbase):
    entire_classbase.append(Course())


def create_initial_admin(entire_userbase):  # Generate a admin to be logged onto so that they may add other students
    # and faculty
    entire_userbase.append(Admin())  # no input parameters to a new admin means that the default is used.
