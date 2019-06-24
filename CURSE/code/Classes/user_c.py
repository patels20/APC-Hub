class User:
    # Base Class that all classes are built off of
    def __init__(self, user_id="", first_name="", last_name="", passcode=""):
        # This is the initialization function
        # if no paramaters are passed into it, the default listed will be used

        self.user_id = user_id          # User ID - It must be UNIQUE
        self.first_name = first_name   # User's First Name
        self.last_name = last_name      # User's Last Name
        self.passcode = passcode        # Passcode is used for initial Login
