import json
from decimal import Decimal
from typing import List, Dict, Callable

TWOPLACES = Decimal(10) ** -2


def print_result(number_to_print: str) -> None:
    """Takes a string of numbers and prints the equivalent glyph.

    Parameters
    ----------
    number_to_print: str
        Number to be printed into a glyph.
    """
    list_of_letters: List[List[str]] = []
    with open("glyph.json") as outfile:
        data: Dict[str, str] = json.load(outfile)

    for letter in number_to_print:
        list_of_letters.append(data[letter].split("\n"))
        list_of_letters.append(data[" "].split("\n"))

    print_glyphs(list_of_letters)


def print_glyphs(list_of_letters: List[List[str]]) -> None:
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


def convert_decimal_into_string(number_to_convert: Decimal) -> str:
    if number_to_convert == number_to_convert.to_integral():
        return str(number_to_convert.quantize(Decimal(1)))

    return str(number_to_convert.quantize(TWOPLACES))


def solve_for_i(p: float, r: float, t: float) -> str:
    """Finds the total amount of interest paid off by the customer over the course of the loan.

    Note
    ----
    P is the amount of money borrowed.
    r is the annual interest rate.
    t is the number of years before the loan is paid off.

    Parameters
    ----------
    P is the amount of money borrowed.
    r is the annual interest rate.
    t is the number of years before the loan is paid off.

    Returns
    -------
    str
        The result of solving for I converted to a string.
    """
    result = Decimal(p*(r/100)*t)

    return convert_decimal_into_string(result)


def solve_for_p(i: float, r: float, t: float) -> str:
    """Finds the total amount of money borrowed.

    Note
    ----
    I is the total amount of interest paid off by the customer over the course of the loan.
    r is the annual interest rate.
    t is the number of years before the loan is paid off.

    Parameters
    ----------


    Returns
    -------
    str
        The result of solving for p converted to a string.
    """
    result = Decimal(i/((r/100)*t))

    return convert_decimal_into_string(result)


def solve_for_r(p: float, i: float, t: float) -> str:
    """Finds the annual interest rate.

    Note
    ----
    I is the total amount of interest paid off by the customer over the course of the loan.
    P is the amount of money borrowed.
    t is the number of years before the loan is paid off.

    Parameters
    ----------


    Returns
    -------
    str
        The result of solving for r converted to a string.
    """
    result = Decimal((i/(p*t))*100)

    return convert_decimal_into_string(result)


def solve_for_t(p: float, r: float, i: float) -> str:
    """Finds the number of years before the loan is paid off.

    Note
    ----
    I is the total amount of interest paid off by the customer over the course of the loan.
    P is the amount of money borrowed.
    r is the annual interest rate.

    Parameters
    ----------


    Returns
    -------
    str
        The result of solving for t converted to a string.
    """
    result = Decimal(i/((r/100)*p))

    return convert_decimal_into_string(result)


def solve_equation(commands: List[str]) -> Callable[[float, float, float], str]:
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


def is_valid_numeric(number: str):
    """Checks if the input is valid.

    Parameters
    ----------


    Returns
    -------
    bool
        True if the input is a number is less than 2 decimal places, False if not.
    """
    try:
        if -2 <= Decimal(number).as_tuple().exponent <= 0:
            return True
        return False
    # If we cant convert to decimal it means it's not a valid input
    except:
        return False


def is_valid_letter(given_argument: str) -> bool:
    correct_arguments = ['r', 't', 'p', 'i']
    return given_argument in correct_arguments


def get_equation_argument_values():
    variables_number_text = ['first', 'second', 'third']
    variables_asked = 0
    commands = {}

    while variables_asked <= 2:
        letter = input(
            "What sort of number is the {} variable? (Please enter i, p, r or t): ".format(variables_number_text[variables_asked]))

        while not is_valid_letter(letter):
            print("Incorrect variable provided, please enter (Please enter i, p, r or t)")
            letter = input(
                "What sort of number is the {} variable? (Please enter i, p, r or t): ".format(variables_number_text[variables_asked]))

        value_of_letter = input(
            "Please now enter the {} variable: ".format(variables_number_text[variables_asked]))

        while not is_valid_numeric(value_of_letter):
            print(
                "Please select a correct number with no more than 2 decimal places.\n")
            value_of_letter = input(
                "Please now enter the {} variable: ".format(variables_number_text[variables_asked]))

        try:
            commands[letter] = int(value_of_letter)
        except ValueError:
            commands[letter] = float(value_of_letter)

        variables_asked += 1

    return commands


def main():

    print("\n")
    print("Welcome to Funky Finance!")

    commands = get_equation_argument_values()

    [first_letter, second_letter, third_letter] = commands.keys()

    print_result(solve_equation(
        [first_letter, second_letter, third_letter])(**commands))


if __name__ == '__main__':
    main()
