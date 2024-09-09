"""Practing conditionals"""


def less_than_10(num: int) -> None:
    """ "Tell us if num<10"""
    if num < 10:  # check if this is true
        print("small number")  # "then" block
    else:
        print("big number")
    print("This is the end of the function")
    # comes after conditonal so will be printed regardless


def wake_up(alarm: bool) -> str:
    """Return a message absed on if alarm is going off"""
    if alarm is True:
        return "Wake up! Go to Comp 110!"
    else:
        return "Keep sleeping, you deserve it"


print(wake_up(alarm=False))
