"""CQ1 Comp110"""

__author__ = "730472090"


def mimic(message: str) -> str:
    """Returning a message"""
    return message


def main() -> None:
    print(mimic(message=input("What is your message?")))
    """Main function to call mimic"""


if __name__ == "__main__":
    main()
