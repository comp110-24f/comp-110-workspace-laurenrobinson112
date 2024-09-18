"""Challege Question Working With While Loops"""

__author__ = "730472090"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count = count + 1
        index = index + 1
    return count


# looping while statement, that goes through each character to see if it matches

num_instances(phrase="HelloHeLloHEllo", search_char="e")
# calling num_instances with a specific phrase and character
