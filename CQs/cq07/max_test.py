__author__ = "730472090"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_mutate() -> None:
    numbers: list[int] = [1, 2, 3, 4, 5]
    assert find_and_remove_max(numbers) == 5  # Returns the max value


def test_find_and_remove_max_return() -> None:
    numbers: list[int] = [1, 2, 3, 4, 5]
    assert find_and_remove_max(numbers) == 5  # Returns the max value
    assert numbers == [1, 2, 3, 4]  # List after removing max, numbers is list


def test_find_and_remove_max_edge() -> None:
    numbers2: list[int] = []
    assert find_and_remove_max(numbers2) == -1


# checking to see if it will return -1 when list is empty
