"""Exercise 0, working on with writing small programs to create a larger program."""

__author__: str = "730472090"


# Have to define tea_count and treat_count here and set them equal
# to a value we have or give the function before running.
# Convert the cost to string so the $ can be added to the final answer


def main_planner(guests: int) -> None:
    """Main planner combines all of the following functions into one
    that allows for easy use"""
    print("A Cozy Tea Party for " + str(guests) + " people!")
    print("tea bags: " + str(tea_bags(people=guests)))
    print("treats: " + str(treats(people=guests)))
    print(
        "Cost: "
        + "$"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Calculating how many tea bags are needed if each person drinks 2"""
    return (people) * 2


def treats(people: int) -> int:
    """Treats function used to determine how many treats people will want, based on
    the amount of tea they are given"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Cost will determine how much money will be spent on the part based on how much
    guests drink and eat"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
# input allows for the person to be prompted with a question,that will then fill
# the number for guest, starting all of the calculations
