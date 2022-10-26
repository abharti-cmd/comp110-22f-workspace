"""EX05!"""

__author__ = "730554167"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_one() -> None:
    """Testing for one even number."""
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]


def test_only_evens_two() -> None:
    """Testing for two even numbers."""
    xs: list[int] = [1, 2, 3, 4]
    assert only_evens(xs) == [2, 4]


def test_only_evens_three() -> None:
    """Testing for three even numbers."""
    xs: list[int] = [1, 2, 4, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_concat_list_one() -> None:
    """Concatenating six elements."""
    xs: list[int] = [1, 2, 3]
    xsx: list[int] = [3, 2, 1]
    assert concat(xs, xsx) == [1, 2, 3, 3, 2, 1]


def test_concat_list_two() -> None:
    """Concatenating seven elements."""
    xs: list[int] = [1, 2, 3, 5]
    xsx: list[int] = [3, 2, 1]
    assert concat(xs, xsx) == [1, 2, 3, 5, 3, 2, 1]


def test_concat_list_three() -> None:
    """Concatenating seven elements."""
    xs: list[int] = [1, 2, 3]
    xsx: list[int] = [3, 2, 1, 0]
    assert concat(xs, xsx) == [1, 2, 3, 3, 2, 1, 0]


def test_sub_list_one() -> None:
    """Sub list with 2 elements."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, 1, 3) == [20, 30]
 
    
def test_sub_list_two() -> None:
    """Sub list with first element."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, 0, 1) == [10]


def test_sub_list_three() -> None:
    """Sub list with an element in the middle."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, 2, 3) == [30]