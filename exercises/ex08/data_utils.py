"""Dictionary related utility functions."""

__author__ = "730554167"

# Define your functions below

from csv import DictReader

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
    for row in table_list: 
        item: str = row[column]
        result.append(item)
    return result