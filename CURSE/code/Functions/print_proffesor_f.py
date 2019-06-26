from Classes.proffesor_c import *

def print_proffesors(userbase):

    for x in userbase:
        if x.__class__ == Proffesor:
            print("\nID: " + x.user_id + "     Name: " + x.first_name + " " + x.last_name)


