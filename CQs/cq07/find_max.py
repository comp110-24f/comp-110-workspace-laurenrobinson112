__author__ = "730472090"


def find_and_remove_max(input: list[int]) -> int:
    if input == []:  # checking to see if list is empty before indexing
        return -1
    index: int = 0
    max: int = input[index]
    while index < len(input):  # going through list to find highest number
        if input[index] > max:
            max = input[index]
        index += 1
    index = 0  # resetting index before 2nd while loop, otherwise it never enters
    while index < len(input):
        if max == input[index]:
            input.pop(index)  # popping index place not value at index (not max)
        else:
            index += 1  # increasing index only if not max because if max it removes,
            # making next number @ same index
    return max
