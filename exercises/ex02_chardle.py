__author__ = "730472090"


def input_word() -> str:
    word: str = input("Enter a 5-character word:")
    if len(word) != 5:  # will send error message if greater or less than 5 characters
        print("Error: Word must contain 5 characters. ")
        print(word)  # did these seperately so the word will print on lower line
        exit()
    else:
        return word


def input_letter() -> str:
    character: str = input("Enter a single character:")
    if len(character) != 1:  # will send error message if not one character
        print("Error: Character must be a single character.")
        exit()
    else:
        return character


def contains_character(word: str, letter: str) -> None:
    index: int = 0
    count: int = 0
    while index < len(word):
        if word[index] == letter:
            print(letter + " is found at index " + str(index))
            count = count + 1
            index += 1
        print(str(count) + " instances of " + letter + " found in " + word)
    else:
        print("No instances of " + letter + " in " + word)


def main() -> None:
    contains_character(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
