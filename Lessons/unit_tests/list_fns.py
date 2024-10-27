"""Using unit tests in class"""


def get_first(Input: list[str]) -> str:
    # return first element
    return Input[0]


def remove_first(Input: list[str]) -> None:
    # remove first element
    Input.pop(0)


def get_and_remove_first(Input: list[str]) -> str:
    # remove and return first element
    first_elem: str = Input[0]
    Input.pop(0)
    return first_elem
