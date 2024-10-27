"""EXO5, testing list functions"""

__author__ = "730472090"

import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens() -> None:
    numbers: list[int] = [1, 2, 3, 4]
    assert only_evens(numbers) == [2, 4]
    assert numbers == [1, 2, 3, 4]


# testing only_evens returns correct values and doesnt modify list in standard cases


def test_only_evens_empty() -> None:
    edge: list[int] = []
    assert only_evens(edge) == []


# testing only_evens returns correct if list is empty


def test_only_evens_odd() -> None:
    odds: list[int] = [1, 3, 5]
    assert only_evens(odds) == []


# testing only_evens returns correct if list is only odd


def test_sub() -> None:
    numbers: list[int] = [1, 2, 3, 4]
    assert sub(numbers, 1, 3) == [2, 3]
    assert numbers == [1, 2, 3, 4]


# testing sub returns correctly and modifies list


def test_sub_empty() -> None:
    assert sub([], 1, 3) == []


# testing sub returns correct if empty list


def test_sub_neg() -> None:
    numbers: list[int] = [1, 2, 3, 4]
    assert sub(numbers, -1, 2) == [1, 2]


# testing sub returns correct if neg start


def test_sub_greater() -> None:
    numbers: list[int] = [1, 2, 3, 4]
    assert sub(numbers, 1, 15) == [2, 3, 4]


# testing sub returns correct if end is too large


def test_add_at_index() -> None:
    numbers: list[int] = [1, 2, 3, 4]
    add_at_index(numbers, 6, 2)
    assert numbers == [1, 2, 6, 3, 4]


# testing add_at_index returns and modifies correctly in typical case


def test_add_at_index_empty() -> None:
    numbers: list[int] = []
    with pytest.raises(IndexError):
        add_at_index(numbers, 1, 1)


# testing add_at_index returns correct if empty lsit


def test_add_at_index_out() -> None:
    numbers: list[int] = [1, 2, 3]
    with pytest.raises(IndexError):
        add_at_index(numbers, 4, 10)


# testing add_at_index returns correctly if out of range
