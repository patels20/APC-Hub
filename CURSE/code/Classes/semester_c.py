from enum import Enum

class trimester(Enum):
    Spring = 1
    Summer = 2
    Fall = 3

class Semester():
    def __init__(self, year, season):
        self.year = year
        self.season = season


