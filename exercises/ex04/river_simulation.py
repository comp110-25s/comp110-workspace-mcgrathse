"""River Simulation of daily life of ecosystem"""

__author__: str = "730642386"


from exercises.EX04.river import River

my_river = River(num_fish=10, num_bears=2)

my_river.view_river()

my_river.one_river_week()

my_river.view_river()
