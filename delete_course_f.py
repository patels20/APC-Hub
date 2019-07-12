from Functions.print_courses_f import print_courses
from Classes.proffesor_c import Proffesor
from Classes.admin_c import Admin

def delete_course(userbase,coursebase):

    # Let the user see what they can delete
    print_courses(coursebase)
    temp = input("\nInput the CRN of the course that needs to be PERMINANTLY deleted:\n")

    for course in coursebase:       # find the class to delete
        if temp == course.crn:

            # remove any dependencies from the whole user base
            for dude in userbase:

                # if the user is a proffessor
                if dude.__class__ == Proffesor:
                    # if the user is a proffesor and there's no course instructor then continue to the next user
                    if course.instructor == "THIS NEEDS TO BE A USER":  # if there is no instructor for the course
                        continue
                if dude.__class__ == Admin:
                    continue

                for indexed_course in dude.crns:
                    # if the Course being deleted is indexed by the user remove the refrence from the proffesor's list of courses
                    if indexed_course == course.crn:
                        dude.crns.remove(indexed_course)
                        print("\nDependency Removed: " + dude.user_id)
                        break
            print("\nCourse Deleted\n")
            coursebase.remove(course)
            # If the course is found then stop looking for courses
            break

