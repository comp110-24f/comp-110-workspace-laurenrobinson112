def remove_chars(msg: str, char: str) -> str:
    """Return copy of msg with instances of char removed"""
    copy: str = ""
    index: int = 0

    while index < len(msg):
        if msg[index] != char:  # not (msg[index] == char)
            copy = copy + msg[index]
        index += 1
    return copy


if __name__ == "__main__":
    word: str = "yoyo"  # global variable
    print(
        remove_chars(word, "y")
    )  # positional argument (putting into parenthesis in order)
    print(remove_chars(word, "o"))
# print(remove_chars(msg="football", char="o"))
# remove_chars("football", "o") -> "ftball"
