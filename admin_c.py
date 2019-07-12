from Classes.user_c import *
# Create an inherited class for the admin:
class Admin(User):
    def __init__(self):
        User.__init__(self, user_id="n", first_name="Grande", last_name="Barriga", passcode="n")
