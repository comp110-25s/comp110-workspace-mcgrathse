"""Plan a Tea Party"""

__author__: str = "730642386"


def main_planner(guests: int) -> None:
    """Tea Party Planner"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_count=guests, treat_count=guests) * 2.6))
    return None


def tea_bags(people: int) -> int:
    """Number of Tea Bags Needed"""
    return people * 2


def treats(people: int) -> int:
    """Number of Treats Needed"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Cost of Tea Bags and Treats"""
    return (tea_bags(people=tea_count) / 2 * 0.5) + (
        treats(people=treat_count) / 3 * 0.75
    )


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
