def chars(msg: str) -> str:
    """Return copy of msg with instances of char removed"""
    idx: int = 0
    copy: str = msg
    while idx < len(msg):
        print(msg[idx])
        idx += 1
    return copy


a: str = "Hey"
b: str = "Hi"
chars(msg=a)
