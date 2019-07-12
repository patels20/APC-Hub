from enum import Enum
class System_state(Enum):  # datatype created to keep track of what state the program is in
    log_on = 1
    run_student = 2  # there will be more of these
    error = 3
    run_admin = 4
    run_proffesor = 5
