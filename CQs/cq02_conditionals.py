"""Using Conditionals to Make a Number Guessing Game """

__author__ = "730472090"


def guess_a_number() -> None:
    secret: int = 7
    number: int = int(input("Guess a number:"))
    print("Your guess was " + str(number))
    if number == secret:
        print("You got it!")
    elif number < secret:
        print(str("Your guess was too low! The secret number is " + str(secret)))
    else:
        print(str("Your guess was too high! The secret number is " + str(secret)))


if __name__ == "__main__":
    guess_a_number()
