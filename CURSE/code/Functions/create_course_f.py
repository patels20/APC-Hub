from Classes.course_c import Course
from Functions.print_proffesor_f import print_proffesors
from Classes.proffesor_c import Proffesor
from Functions.print_courses_f import print_courses


def create_course(coursebase, userbase, activeuser):
    new_course = Course(input("\nInput CRN: \n"), input("Input Course Name: \n"), "THIS NEEDS TO BE A USER",
                        input("\nInput the number of hours the course is:\n"),
                        int(input("Input Max number of students: \n")), input("\nInput Major: \n"),
                        input("\nInput required grade\n"))
    kgrab = ""
    while kgrab != "0":
        print_courses(coursebase)
        kgrab = input(
            "\nInput the crn of a prerequisite of this class: \nOr enter '0' to stop adding required courses\n")

        for course in coursebase:
            if kgrab == course.crn:
                new_course.restrictions.append(kgrab)
                print("\nRestriction added\nTotal Restrictions:")
                for x in new_course.restrictions:
                    print(" " + x)
                print("\n")

    print_proffesors(userbase)  # print the professor so that it is easier to see who you are assigning
    temp = input("\nInput the ID of the professor for this new course: \nInput 0 if no proffesor\n")

    if temp != "0":
        for teacher in userbase:
            if teacher.__class__ == Proffesor:  # if the user id matches a teacher
                if temp == teacher.user_id:
                    new_course.instructor = teacher.user_id  # add the teacher to the class data
                    new_course.print_course()  # print the new course created
                    coursebase.append(new_course)  # Update the database
                    print("I make it here")
                    teacher.crns.append(new_course.crn)  # Update the user in database
                    break
    else:
        print("course added to database without an instructor")  # if the input didn't match an ID
        new_course.print_course()
        coursebase.append(new_course)

    return
