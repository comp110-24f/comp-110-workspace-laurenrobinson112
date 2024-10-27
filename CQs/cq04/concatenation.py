"""Challege Question 4: Importing"""

__author__ = "730472090"


def concat(word1: str, word2: str) -> str:
    return word1 + word2  # concatonates word1 and word2


# making word1 and word2 global variables
word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":
    print(concat("happy", " tuesday"))
# using this so that the function does not run completely when imported
