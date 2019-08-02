from enum import Enum

class trimester(Enum):
    Spring = 1
    Summer = 2
    Fall = 3

class Semester():
    def __init__(self):
        self.year = 2000
        self.season = trimester.Fall
