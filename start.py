import json
from decimal import Decimal

TWOPLACES = Decimal(10) ** -2


def print_result(number_to_print):
    """Takes a string of numbers and prints the equivalent glyph.

    Parameters
    ----------
    number_to_print: str
        Number to be printed into a glyph.
    """
    data = {}
    list_of_letters = []
    with open("glyph.json") as outfile:
        data = json.load(outfile)

    for letter in number_to_print:
        list_of_letters.append(data[letter].split("\n"))
        list_of_letters.append(data[" "].split("\n"))

    print_glyphs(list_of_letters)


def print_glyphs(list_of_letters):
    """Prints into the screen the combination of a list of glyphs.

    Parameters
    ----------
    list_of_letters: list(list(str))
        List of glyphs to be printed.
    """
    for row in list(zip(*list_of_letters)):
        text = ""
        for letter in row:
            text = text + letter
        print(text)


def solve_for_i(**letters):
    """Finds the total amount of interest paid off by the customer over the course of the loan.

    Note
    ----
    P is the amount of money borrowed.
    r is the annual interest rate.
    t is the number of years before the loan is paid off.

    Parameters
    ----------
    letters
        Commands keyword arguments.

    Returns
    -------
    str
        The result of solving for I converted to a string.
    """
    p = letters["p"]
    r = letters["r"]
    t = letters["t"]
    result = Decimal(p*(r/100)*t)

    if (result == result.to_integral()):
        return str(result.quantize(Decimal(1)))

    return str(result.quantize(TWOPLACES))


def solve_for_p(**letters):
    """Finds the total amount of money borrowed.

    Note
    ----
    I is the total amount of interest paid off by the customer over the course of the loan.
    r is the annual interest rate.
    t is the number of years before the loan is paid off.

    Parameters
    ----------
    letters
        Commands keyword arguments.

    Returns
    -------
    str
        The result of solving for p converted to a string.
    """
    i = letters["i"]
    r = letters["r"]
    t = letters["t"]
    result = Decimal(i/((r/100)*t))

    if (result == result.to_integral()):
        return str(result.quantize(Decimal(1)))

    return str(result.quantize(TWOPLACES))


def solve_for_r(**letters):
    """Finds the annual interest rate.

    Note
    ----
    I is the total amount of interest paid off by the customer over the course of the loan.
    P is the amount of money borrowed.
    t is the number of years before the loan is paid off.

    Parameters
    ----------
    letters
        Commands keyword arguments.

    Returns
    -------
    str
        The result of solving for r converted to a string.
    """
    p = letters["p"]
    i = letters["i"]
    t = letters["t"]
    result = Decimal((i/(p*t))*100)

    if (result == result.to_integral()):
        return str(result.quantize(Decimal(1)))

    return str(result.quantize(TWOPLACES))


def solve_for_t(**letters):
    """Finds the number of years before the loan is paid off.

    Note
    ----
    I is the total amount of interest paid off by the customer over the course of the loan.
    P is the amount of money borrowed.
    r is the annual interest rate.

    Parameters
    ----------
    letters
        Commands keyword arguments.

    Returns
    -------
    str
        The result of solving for t converted to a string.
    """
    p = letters["p"]
    r = letters["r"]
    i = letters["i"]
    result = Decimal(i/((r/100)*p))

    if (result == result.to_integral()):
        return str(result.quantize(Decimal(1)))

    return str(result.quantize(TWOPLACES))


def solve_equation(commands):
    """Function that takes a list of commands and returns the correct solving function
    that maps to those arguments.

    Parameters
    ----------
    commands: list(str)
        List of letters provided by the user.

    Returns
    -------
    func
        The corresponding solving function.
    """
    available_commands = ['i', 'r', 't', 'p']
    # get the missing argument
    my_command = list(set(available_commands) - set(commands))[0]

    if my_command == 'i':
        return solve_for_i

    if my_command == 'p':
        return solve_for_p

    if my_command == 'r':
        return solve_for_r

    if my_command == 't':
        return solve_for_t


def is_valid_numeric(input):
    """Checks if the input is valid.

    Parameters
    ----------
    commands: str
        String input that represents a number

    Returns
    -------
    bool
        True if the input is a number is less than 2 decimal places, False if not.
    """
    try:
        if -2 <= Decimal(input).as_tuple().exponent <= 0:
            return True
        return False
    # If we cant convert to decimal it means it's not a valid input
    except:
        return False


def is_valid_letter(given_argument):
    correct_arguments = ['r', 't', 'p', 'i']
    return given_argument in correct_arguments


def main():
    commands = {}

    print("\n")
    print("Welcome to Funky Finance!")

    # Ask the user for the first letter and variable
    first_letter = input(
        "What sort of number is the first variable? (Please enter i, p, r or t): ")
    while not is_valid_letter(first_letter):
        print("Incorrect variable provided, please enter (Please enter i, p, r or t)")
        first_letter = input(
            "What sort of number is the first variable? (Please enter i, p, r or t): ")

    first_variable = input(
        "Please now enter the first variable: ")
    # If the user fails to follow the format, we display an error message and try again
    while not is_valid_numeric(first_variable):
        print(
            "Please select a correct number with no more than 2 decimal places.\n")
        first_variable = input(
            "Please now enter the first variable: ")
    # Convert variable into an integer or a float
    try:
        commands[first_letter] = int(first_variable)
    except ValueError:
        commands[first_letter] = float(first_variable)

    # Ask the user for the second letter and variable
    second_letter = input(
        "What sort of number is the second variable? (Please enter i, p, r or t): ")
    while not is_valid_letter(second_letter):
        print("Incorrect variable provided, please enter (Please enter i, p, r or t)")
        second_letter = input(
            "What sort of number is the second variable? (Please enter i, p, r or t): ")

    second_variable = input(
        "Please now enter the second variable: ")
    # If the user fails to follow the format, we display an error message and try again
    while not is_valid_numeric(second_variable):
        print(
            "Please select a correct number with no more than 2 decimal places.\n")
        second_variable = input(
            "Please now enter the second variable: ")
    # Convert variable into an integer or a float
    try:
        commands[second_letter] = int(second_variable)
    except ValueError:
        commands[second_letter] = float(second_variable)

    # Ask the user for the third letter and variable
    third_letter = input(
        "What sort of number is the third variable? (Please enter i, p, r or t): ")
    while not is_valid_letter(third_letter):
        print("Incorrect variable provided, please enter (Please enter i, p, r or t)")
        third_letter = input(
            "What sort of number is the third variable? (Please enter i, p, r or t): ")

    third_variable = input(
        "Please now enter the third variable: ")
    # If the user fails to follow the format, we display an error message and try again
    while not is_valid_numeric(third_variable):
        print(
            "Please select a correct number with no more than 2 decimal places.\n")
        third_variable = input(
            "Please now enter the third variable: ")
    # Convert variable into an integer or a float
    try:
        commands[third_letter] = int(third_variable)
    except ValueError:
        commands[third_letter] = float(third_variable)

    print_result(solve_equation(
        [first_letter, second_letter, third_letter])(**commands))


if __name__ == '__main__':
    main()
