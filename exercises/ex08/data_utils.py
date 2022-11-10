"""Dictionary related utility functions."""

__author__ = "730554167"

# Define your functions below

from csv import DictReader
from re import I

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read an entire CSV of data into a list of rows."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
        file_handle.close()

        return result 
    

def column_values(table_list: list[dict[str, str]], column: list[str]) -> list[str]:
    """Produces a list of all values in a single column whose name is the second parameter"""
    result: list[str] = []
    i = 0
    for i in table_list: 
        result.append(i[column])
    return result


def columnar(table_1: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms a table into a dictionary of columns."""
    result: dict[str, list[str]] ={}
    for empty in table_1[0]:
        result[empty] = []

    for row in table_1:
        for key in row:
            result[key].append(row[key])
    return result


def head(column: dict[str, list[str]], row: int) -> dict[str, list[str]]:
    """Creates a column-based table """