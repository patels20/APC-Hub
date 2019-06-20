# Ameer Noufal
# APC - Assignment 1
from array import *

# Username and password portion:
# Test username and password for a basic version of the program.
username = "anoufal"
password = "ameer"
loginchoice = 0


class student:
    # declare the components of a student:
    name = 0
    major = 0
    crns = array('i')

    def setname(self, inputname):
        self.name = inputname

    def setmajor(self, inputmajor):
        self.major = inputmajor

    def setcrns(self, inputcrns):
        self.crns = inputcrns

    def printstudent(self):
        print("the students name is ", self.name, " their major is ", self.major, " and the CRN(s) are ", self.crns)


def printmenu():
    print("1. add a student")
    print("2. print ")


# Print the menu to sign into the CURSE system
def printloginmenu():
    print("Welcome! Please login below:")
    loginchoice = input("would you like to log in? (1 = yes)")
    if loginchoice == 1:
        loginuser()
    else:
        exit


def loginuser():
    userinput = input("what is your username?")
    if userinput == username:
        user_pass = input("what is the password?")
        if user_pass == password:

            print("thats correct, Welcome!!")
            mainmenu()
        else:
            printloginmenu()
    else:
        printloginmenu()


def mainmenu():
    print("Welcome to the curse registration system! thank you for signing in " + username + "!!\n")


# BEGIN THE MAIN CODE HERE:
# **********************************************************************************
# while loop to make the program continuous
motivator = 1

classroster = []

while motivator == 1:

    printloginmenu()
    print("here are your options")

    # print the menu
    printmenu()

    choice = eval(input("what would you like to do?"))

    # if statement to make a completely new student
    if choice == 1:
        newstudent = student()
        inputname = input("what is their name?")
        newstudent.setname(inputname)
        inputmajor = input("what is their major? ")
        newstudent.setmajor(inputmajor)
        inputcrns = list(map(int, input("enter the CRN(S) the student is enrolled in").split()))
        # inputcrns = eval(input("what is the CRN(s)"))
        newstudent.setcrns(inputcrns)

        classroster.append(newstudent)

    # print(classroster[0].printstudent())
    elif choice == 2:

        print("test")
        for i in classroster:
            i.printstudent()
