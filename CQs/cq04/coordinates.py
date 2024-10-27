"""Challege Question 4: Importing"""

__author__ = "730472090"


def get_coords(xs: str, ys: str) -> None:
    indexx: int = 0
    indexy: int = 0
    while indexx < len(xs):
        while indexy < len(ys):
            print("(" + xs[indexx] + "," + ys[indexy] + ")")
            indexy += 1
        indexx += 1
        indexy = 0  # need to set it back to zero for returning to x variable counting


# use indexx and indexy to differentiate between couting the x and y variables
