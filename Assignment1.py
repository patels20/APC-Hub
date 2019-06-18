# Ameer Noufal
# APC - Assignment 1
from array import * 

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


# while loop to make the program continuous
motivator =1

 # import array as arr

classroster =[]
while motivator == 1:

	print("here are your options")

	# print the menu
	printmenu()

	choice = eval(input("what would you like to do?"))

	# if statement to make a completely new student
	if choice ==1:
		newstudent = student()
		inputname = input("what is their name?")
		newstudent.setname(inputname)
		inputmajor = input("what is their major? ")
		newstudent.setmajor(inputmajor)
		inputcrns = list(map(int, input("enter the CRN(S) the student is enrolled in").split()))
		# inputcrns = eval(input("what is the CRN(s)"))
		newstudent.setcrns(inputcrns)

		classroster.append(newstudent)

		#print(classroster[0].printstudent())
	elif choice == 2:

		print("test")
		for i in classroster:

			i.printstudent()
