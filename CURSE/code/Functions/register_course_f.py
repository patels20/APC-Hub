def register_course(coursebase, userbase, activeuser):
    #  This function has the user input a CRN-
    #  code and attempts to register for it

    temp = input("Input the crn value of the course you want to register :\n")
    for course in coursebase:
        if temp == course.crn:                      # if the course exists attempt to register the active user
            #this function will check if the student can be added to the course and return a 1 if successfull
            if course.add_student(activeuser[0]):      # Execute this code if the student is able to be registered
                for dude in userbase:           #finds the user in the database
                    if dude == activeuser[0]:
                        dude.add_course(temp)   # adds the crn code to the database
                        activeuser[0] = dude    # updates the active user data
                        print("\nsuccessfuly registered for:" + temp + "\n")
                        return                  # Stops the method because the task is done
                print("\nSTUDENT ADDED TO COURSE ROSTER BUT COURSE NOT ADDED TO STUDENT SCHEDULE\nThis should never happen\n")
            return # return if the course requested is at capacity
    print("\nFailed to register\n")
    return
