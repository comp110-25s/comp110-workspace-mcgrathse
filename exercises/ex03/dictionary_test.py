"""Unit Tests for dictionary functions"""

__author__: str = "730642386"


from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_favorite_color() -> None:
    """Use Case Test 1 for favorite_color"""
    assert favorite_color({"Sarah": "blue", "Morgan": "white", "Diya": "red"}) == "blue"


def test_favorite_color_use() -> None:
    """Use case Test 2 for favorite_color"""
    assert favorite_color({"Sarah": "red", "Morgan": "white", "Diya": "red"}) == "red"


def test_favorite_color_edge() -> None:
    """Edge case Test for favorite_color"""
    favorite_colors = {
        "Sarah": "red",
        "Morgan": "white",
        "Diya": "red",
        "Chloe": "white",
    }
    assert favorite_color(favorite_colors) == "red"


def test_invert() -> None:
    """Use case test 1 for invert"""
    assert invert({"Sarah": "blue"}) == {"blue": "Sarah"}


def test_invert_use() -> None:
    """Use case test 2 for invert"""
    assert invert({"Morgan": "white", "Sarah": "blue"}) == {
        "white": "Morgan",
        "blue": "Sarah",
    }


def test_invert_edge() -> None:
    """Edge case test for invert"""
    assert invert({}) == {}


def test_count() -> None:
    """Use case test 1 for count"""
    items = ["pen", "paper", "marker"]
    prove = count(items)
    correct = {"pen": 1, "paper": 1, "marker": 1}
    assert prove == correct


def test_count_two() -> None:
    """Use case test 2 for count"""
    animals = ["lion", "cat", "lion"]
    test = count(animals)
    correct_new = {"lion": 2, "cat": 1}
    assert test == correct_new


def test_count_edge() -> None:
    """Edge case test for count"""
    plants = []
    test_edge = count(plants)
    correct_edge = {}
    assert test_edge == correct_edge


def test_bin_len() -> None:
    """Use case test 1 for bin_len"""
    numbers = ["one", "two", "three", "four"]
    assert bin_len(numbers) == {3: {"one", "two"}, 5: {"three"}, 4: {"four"}}


def test_bin_len_use() -> None:
    """Use case test 2 for bin_len"""
    names = ["kyle", "matt"]
    assert bin_len(names) == {4: {"kyle", "matt"}}


def test_bin_len_edge() -> None:
    """Edge case test for bin_len"""
    empty = []
    assert bin_len(empty) == {}
