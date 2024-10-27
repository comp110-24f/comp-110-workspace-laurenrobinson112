"""Practicing List Functions"""

__author__ = "730472090"


def all(Input: list[int], target: int) -> bool:
    if len(Input) == 0:
        return False
    for elem in Input:
        if elem != target:
            return False
    return True


# using for... in... loop to check if the value in list is equal to the target value

# print(all([1, 1, 1], 2))


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    # used to return an error value when there is no list
    max_value: int = input[0]
    for elem in input:
        if elem > max_value:
            max_value = elem
    return max_value


# using loop to check if the max_value is still the first value, if not replaces
# with new max

# print(max([300, 100, 40]))


def is_equal(L_1: list[int], L_2: list[int]) -> bool:
    if len(L_1) != len(L_2):
        return False
    for idx in range(len(L_1)):
        if L_1[idx] != L_2[idx]:
            return False
    return True


# using loop to see if index values are the same in each list
# return False is one is not
# print(is_equal(L_1=[1, 2, 3, 5], L_2=[1, 2, 3]))


def extend(list_1: list[int], list_2: list[int]) -> None:
    for elem in list_2:
        list_1.append(elem)


# adds list_2 to the end of list_1
