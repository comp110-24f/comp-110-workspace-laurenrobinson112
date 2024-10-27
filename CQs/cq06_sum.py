"""Summing the elements of a list using different loops"""

__author__ = "730472090"


def w_sum(vals: list[float]) -> float:
    index: int = 0
    sum: float = 0.0
    while index < len(vals):  # summing using while loop
        sum += vals[index]
        index += 1
    return sum


# w_sum(vals=[1.0, 2.0, 3.0])


def f_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for elem in vals:  # summing using for... in... function
        sum += (
            elem  # elem refers to the element in the list when using just for in loop
        )
    return sum


# f_sum(vals=[1.0, 2.0, 3.0])


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for idx in range(0, len(vals)):  # summing using for... in range... function
        sum += vals[idx]  # idx refers to index in list when range function is used
    return sum


# f_range_sum(vals=[1.0, 2.0, 3.0])
