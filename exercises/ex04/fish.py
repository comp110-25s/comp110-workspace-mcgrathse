"""File to define Fish class."""

__author__: str = "730642386"


class Fish:
    age: int

    def __init__(self, age: int):
        "Establishes age default for fish"
        self.age = 0
        return None

    def one_day(self):
        """Increases fish age by 1"""
        self.age += 1
        return None
