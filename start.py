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
    listOfLetters = []
    with open("glyph.json") as outfile:
        data = json.load(outfile)

    for letter in number_to_print:
        listOfLetters.append(data[letter].split("\n"))
        listOfLetters.append(data[" "].split("\n"))

    print_glyphs(listOfLetters)


def print_glyphs(listOfLetters):
    """Prints into the screen the combination of a list of glyphs.

    Parameters
    ----------
    listOfLetters: list(list(str))
        List of glyphs to be printed.
    """
    for row in list(zip(*listOfLetters)):
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


