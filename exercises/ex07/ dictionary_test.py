"""EX07!"""

__author__ = "730554167"

from exercises.ex07.dictionary import invert, favorite_color, count
import pytest 


def test_invert_1() -> None:
    """Testing a dictionary."""
    dictionary: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(dictionary) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_2() -> None:
    """Testing a shorter dictionary."""
    dictionary: dict[str, str] = {'apple': 'cat'}
    assert invert(dictionary) == {'cat': 'apple'}


def test_invert_3() -> None:
    """Third testing."""
    dictionary: dict[str, str] = {'kris': 'jordan', 'michael': 'jorda'}
    assert invert(dictionary) == {'jordan': 'kris', 'jorda': 'michael'}


with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)
# testing for NameError


def test_favorite_color_1() -> None:
    """First Test."""
    dictionary: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Arya": "yellow", "Shiv": "yellow"}
    assert favorite_color(dictionary) == "yellow"


def test_favorite_color_2() -> None:
    """Second Test with numbers."""
    dictionary: dict[str, str] = {"1": "go", "2": "go", "3": "e", "4": "blue", "5": "6"}
    assert favorite_color(dictionary) == "go"


def test_favorite_color_3() -> None:
    """Shorter Third Test with 3 pairs."""
    dictionary: dict[str, str] = {"Far": "yes", "Close": "Yes", "3": "yes"}
    assert favorite_color(dictionary) == "yes"
# testing for favoroite_color


def test_count_1() -> None: 
    """First Test."""
    list_1: list[str] = ["Hi", "Bye", "Hi"]
    assert dict(count(list_1)) == {"Hi": 2, "Bye": 1}


def test_count_2() -> None: 
    """Second Test."""
    list_1: list[str] = ["Praj", "Shiv", "Friends", "Praj", "Praj"]
    assert dict(count(list_1)) == {"Praj": 3, "Shiv": 1, "Friends": 1}


def test_count_3() -> None: 
    """Third Test."""
    list_1: list[str] = ["Praj", "Makes", "Me", "Khush", "Praj", "Wal"]
    assert dict(count(list_1)) == {"Praj": 2, "Make": 1, "Me": 1, "Wal": 1}
# testing for count