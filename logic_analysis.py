import os
import sys

# Semantic logical operations
CONJUNCTION = "^"
INCLUSIVE_DISJUNCTION = "v"
EXCLUSIVE_DISJUNCTION = []
MATERIAL_IMPLICATION = "->"
MATERIAL_EQUIVALENCE = "<->"
NEGATION = "~"


def main():
    """
    This program will ask the user for a set of premises, and a conclusion.
    It will then attempt to derive the conclusion from the premises using legal logical
    operations from natural deduction.
    If it found any such valid solutions, it will display them afterwards.
    :return: None
    """
    platform = initialize()

    premises = get_premises(platform)
    conclusion = get_conclusion()

    valid_solutions = find_valid_solutions(premises, conclusion)

    if len(valid_solutions) < 1:
        print("There are no possible solutions. This is logically invalid")
    else:
        print("Here are some valid solutions:")


def initialize():
    """
    Finds the type of OS running.
    Returns that information.
    :return: platform (str)
    """
    platform = sys.platform
    if platform == "win32":
        platform = "Windows"
    elif platform == "linux":
        platform = "Linux"

    return platform


def get_premises(platform):
    """
    Asks the user to input a new premise until he has entered "done" or an empty string. The new premise is appended to
    a list of premises, which is updated and shown each time the user has finished dding a new premise.
    :param platform: The operating system the user is running (used for clearing the console properly).
    :type platform: str
    :return: premises (list)
    """
    premises = []

    is_done = False
    while not is_done:
        clear_console(platform)
        print("Current premises:")
        for premise in premises:
            print(premise)
        print("\n")
        new_premise = input("To add another premise, start typing [type done if finished adding new premises]: ")
        if new_premise == "done" or new_premise == "DONE" or new_premise == "Done" or new_premise == "":
            is_done = True
        else:
            premises.append(new_premise)

    return premises


def clear_console(platform):
    """
    Clears the console according to the operating system being used.
    :param platform: The operating system the user is running (used for clearing the console properly).
    :type platform: str
    :return: None
    """
    if platform == "Windows":
        os.system("cls")
    elif platform == "Linux":
        os.system("clear")


def get_conclusion():
    """
    Asks the user to input the conclusion and then returns it.
    :return: conclusion (str)
    """
    conclusion = input("Now please input the conclusion: ")

    return conclusion


def find_valid_solutions(premises, conclusion):
    """
    Attempts to derive the conclusion from the premises using several techniques.
    If successful, it stores the set of steps used for each technique as a list in a list.
    :param premises: The premises entered by the user.
    :type premises: list of str
    :param conclusion: The conclusion entered by the user.
    :type conclusion: str
    :return: valid_solutions (list of list)
    """
    valid_solutions = []

    return valid_solutions


if __name__ == '__main__':
    main()
