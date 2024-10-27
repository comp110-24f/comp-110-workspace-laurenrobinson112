"""EXO5, practicing list functions"""

__author__ = "730472090"


def only_evens(input: list[int]) -> list:
    Even: list[int] = []
    for number in input:  # looking in list for all numbers, returns lsit of evens
        if number % 2 == 0:
            Even.append(number)
    return Even


def sub(a_list: list[int], start: int, end: int) -> list:
    subset: list[int] = []
    if len(a_list) == 0 or start >= len(a_list) or end <= 0:
        return subset  # taking care of edge cases
    if start < 0:
        start = 0
    if end > len(a_list):
        end = len(a_list)
    for idx in range(
        start, end
    ):  # make sure to append the number @ index, not the index itself
        subset.append(a_list[idx])
    return subset


def add_at_index(input: list[int], elem: int, index: int) -> None:
    if index < 0 or index > len(input):  # returns index error if out of range
        raise IndexError("Index is out of bounds for the input list")
    input.append(0)
    idx = len(input) - 1  # starts at 0 so index is len -1
    while idx > index:
        input[idx] = input[idx - 1]
        idx -= 1
    input[index] = elem
