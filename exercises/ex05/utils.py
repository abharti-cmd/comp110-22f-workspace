"""EX05!"""

__author__ = "730554167"


def only_evens(evens: list[int]) -> int:
    """Outputs all even integers."""
    output = []
    for i in range(len(evens)):
        if (evens[i] % 2 == 0):
            output.append(evens[i])
    return output 


def concat(list_one: list[int], list_two: list[int]) -> int: 
    """Combines the two lists."""
    new_list = list_one + list_two
    return new_list


def sub(list: list[int], start: int, end: int) -> int:
    """Returns shorten list."""
    output = []
    if start < 0:
        start = 0
    if end > len(list):
        end = len(list)
    while start < end:
        output.append(list[start])
        start += 1
    return output