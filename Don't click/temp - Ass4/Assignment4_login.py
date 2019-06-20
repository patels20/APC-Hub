# Ameer Noufal



# Username and password portion:
# Test username and password for a basic version of the program.
username = "anoufal"
password = "ameer"


# Print the menu to sign into the CURSE system
def printloginmenu():
    print("Welcome! Please login below:")
    choice = input("would you like to log in? (Y = yes)")
    if choice == "Y":
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

# Main part of the code:

motivator =1

while motivator == 1:
    printloginmenu()
