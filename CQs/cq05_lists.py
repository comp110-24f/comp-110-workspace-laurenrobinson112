"""Mutating functions."""

__author__ = "730472090"


def manual_append(Input: list[int], num: int) -> None:
    Input.append(num)  # adding num to the end of input


def double(Input: list[int]) -> None:
    index: int = 0
    while index < len(Input):
        Input[index] *= 2  # multiplying every part of list by 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)  # calling double with input list_2
print(list_2)
print(list_1)
