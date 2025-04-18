"""File to define Bear class."""

__author__: str = "730642386"


class Bear:
    age: int
    hunger_score: int

    def __init__(self, age: int, hunger_score: int):
        """Sets age and hunger score for bears"""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Increases bear age by 1"""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Establishes bear hunger score increases by amount of fish"""
        self.hunger_score += num_fish
