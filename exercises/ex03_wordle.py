"""Creating a World using while loops"""

__author__ = "730472090"


def input_guess(secret_word_len: int) -> str:
    """Get input word and check if it is correct length"""
    word: str = input(f"Enter a {secret_word_len} character word:")
    while len(word) != secret_word_len:
        # will tell if length of word is not same length of secret_word
        word = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return word


"""Looking for occurances of character in guess, which will be a word"""


def contains_char(secret_word: str, character: str) -> bool:
    assert len(character) == 1  # ensuring character guess is 1 letter
    index: int = 0
    while index < len(secret_word):
        if secret_word[index] == character:
            return True
        index += 1
    return False  # returns false if character is not found in secret_word


"""Will look through secret_word and return emojis based on whether guess
matches any characters"""
# adds codes for emojis when these are called
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    index: int = 0
    emojis: str = ""  # this is where emojis will be added when theres a guess
    while index < len(guess):
        if guess[index] == secret[index]:
            emojis += GREEN_BOX
            # adds green box emoji if the guessed character matches index in word
        elif contains_char(secret, guess[index]):
            emojis += YELLOW_BOX
        else:
            emojis += WHITE_BOX
        index += 1
    return emojis


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1  # counts how many guesses theyve made
    max: int = 6  # how many guesses they can make
    won: bool = False
    while turns <= max and not won:
        print(f"=== Turn {turns}/{max} ===")
        guess: str = input_guess(len(secret))
        # calls what they guessed from earlier, to look at length of the secret_word
        result: str = emojified(guess, secret)
        # uses emojified to add the colored boxes to printed results
        print(result)
        if guess == secret:
            print(f"You won in {turns}/{max} turns!")
            won = True  # used if they guess the correct word
        else:
            turns += 1  # used if correct word is not guessed, will continue game
    if not won:
        print(f"X/{max} - Sorry, try again tomorrow!")
        won = False


if __name__ == "__main__":
    main(secret="codes")


# secret_word: str = "Happy"
# print(contains_char("abc", "b"))
# print(input_guess())
