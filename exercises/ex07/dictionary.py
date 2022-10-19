"""EX07."""

__author__ = "730554167"


def invert(GivenDict: dict[str, str]) -> dict[str, str]:
    """Reverses the values in a dictionary."""
    emp = {}

    for givenKey in GivenDict:
        if GivenDict[givenKey] in emp.keys():
            raise KeyError("This key already exists")
        emp[GivenDict[givenKey]] = givenKey
    return emp
# invert function that will reverse the key and values of a dictions and return the reversed dictionary 


def favorite_color(AddedDict: dict[str, str]) -> str:
    """Returns the most frequent color."""
    emp = {}
    frequent_color = ""
    frequency = 0
    for i in AddedDict:
        if AddedDict[i] in emp:
            emp[AddedDict[i]] = emp[AddedDict[i]] + 1
        else:
            emp[AddedDict[i]] = 1
    for i in emp:
        if emp[i] > frequency:
            frequent_color = i
            frequency = emp[i]
    return frequent_color
# favorite_color function that will return the most frequent color 


def count(list_1: list[str]) -> dict[str, int]:
    """Creates a dictionary based on the inputed sting with unique keys."""
    emp = {}
    counter = 0
    for i in list_1:
        if i in emp:
            emp[list_1[counter]] += 1
        else:
            emp[list_1[counter]] = 1
        counter += 1
    return emp