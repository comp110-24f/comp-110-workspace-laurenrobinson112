__author__ = "730472090"


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    if len(word) != 5:  # will send error message if greater or less than 5 characters
        print("Error: Word must contain 5 characters.")
        print(word)  # did these seperately so the word will print on lower line
        exit()  # makes it so rest of code wont run if this error message is sent
    else:
        return word


def input_letter() -> str:
    character: str = input("Enter a single character: ")
    if len(character) != 1:  # will send error message if not one character
        print("Error: Character must be a single character.")
        exit()
    else:
        return character


def contains_char(word: str, letter: str) -> None:
    index: int = 0
    count: int = 0
    print("Searching for " + letter + " in " + word)
    while index < len(word):
        if word[index] == letter:
            print(letter + " found at index " + str(index))
            count = count + 1
        index += 1  # Increasing index to avoid infinite loop

    if count > 0:  # put if statement out here so it won't print every time loops runs
        if count == 1:
            print(str(count) + " instance of " + letter + " in " + word)
        else:
            print(str(count) + " instances of " + letter + " found in " + word)
    else:
        print("No instances of " + letter + " in " + word)


def main() -> None:
    word: str = input_word()
    letter: str = input_letter()
    contains_char(word, letter)


# setting my variables equal so that all functions will be called

if __name__ == "__main__":
    main()
