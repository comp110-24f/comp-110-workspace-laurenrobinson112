"""Practicing Dictionaries"""

__author__ = "730472090"


def invert(words: dict[str, str]) -> dict[str, str]:
    new_dict: dict[str, str] = {}
    for key in words:
        if words[key] in new_dict:  # checking if the key is already in dict
            raise KeyError("Cannot have two of the same keys!")
        new_dict[words[key]] = key
    return new_dict


def favorite_color(favorites: dict[str, str]) -> str:
    counts: dict[str, int] = {}  # dict for the counts of each color
    most_popular: str = []  # writing the most popular color as a str
    max_count: int = 0  # counting how many people said it was their favorite color
    for name in favorites:
        color = favorites[
            name
        ]  # setting color equal to the specific cool we're looking at
        if color in counts:
            counts[color] += 1  # is exist in list add one
        else:
            counts[color] = 1  # if not you create it and start it at one
    for name in favorites:
        color = favorites[name]
        if counts[color] > max_count:  # sets max count equal to current largest value
            most_popular = color
            max_count = counts[color]
    return most_popular


def count(numbers: list[str]) -> dict[str, int]:
    value_counts: dict[str, int] = {}
    for number in numbers:
        if number in value_counts:  # if the value is already in our list, add 1
            value_counts[number] += 1
        else:  # if value not in list, start it at one
            value_counts[number] = 1
    return value_counts


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    letter_count: dict[str, list[str]] = {}
    for word in words:
        letter = word[0].lower()  # setting letter equal to the first letter in a word
        if letter not in letter_count:
            letter_count[letter] = (
                []
            )  # creating empty list to add words to for new letter
        letter_count[letter].append(word)  # addings words to the values for that letter
    return letter_count


def update_attendance(days: dict[str, list[str]], day: str, student: str) -> None:
    if day in days:  # checking if day is already in days, if not will add
        if (
            student not in days[day]
        ):  # adding student to the dict for the day (value for the key)
            days[day].append(student)
    else:
        days[day] = [student]
