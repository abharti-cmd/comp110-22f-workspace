<<<<<<< HEAD
"""EX04 - ."""
=======
"""EX04!"""
>>>>>>> b6be37cd7d149ead1ec73c51851389ad1c519d96

__author__ = "730554167"


<<<<<<< HEAD
def all(InputList: list[str], character: str) -> bool:
    i: int = 0
    print(character)
    while i < len(InputList):
        if InputList[1] == int:
            return True
        i += 1
    return False
=======
def all(list: list[str], character: str) -> bool:
    """Returns true or false if the character is present or not."""
    i = 0 
    while i < len(list): 
        if list[i] == str(character):
            i += 1
        else: 
            return False 
    return True 
    


def max(inputs: list[int]) -> int:
    """Returns the max value."""
    x = 0 
    greatest = -9999 
    while x < len(inputs): 
        if greatest < (inputs[x]): 
            greatest = (inputs[x])
        x += 1
    return greatest
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")


def is_equal(list_one: list[str], list_two: list[str]) -> bool:
    """Shows if lists are equal or not."""
    while len(list_one) == len(list_two):
        if list_one == list_two: 
            return True 
        else: 
            return False 
    return False 
>>>>>>> b6be37cd7d149ead1ec73c51851389ad1c519d96
