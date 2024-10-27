"""Practice lists in class"""

my_numbers: list[float] = []  # with literal
my_numbers: list[float] = list()  # with constructor

my_numbers.append(1.5)  # adding an item to the list
my_numbers.append(2.3)

# print(my_numbers)

# create an already populated list
game_points: list[int] = [102, 86, 94]

# subscription notation, indexing
# print(game_points[2])
last_game: int = game_points[2]  # saving this value as a variable

# modifying parts of list, function at index then = new value
# can do because lists are mutable, strings are not
game_points[1] = 72
# print(game_points)

# getting length
# print(len(game_points))
y: int = len(game_points)

# removing a variable
game_points.pop(1)
# print(game_points)


# write a function called display
# Input: list[int]
# Return value: None
# Loop over the input and print every value
# Try calling it on game_points


def display(Input: list[int]) -> None:
    index: int = 0
    input(list[int])
    while index < len(Input):
        print(Input[index])
        index += 1


display(Input=game_points)
