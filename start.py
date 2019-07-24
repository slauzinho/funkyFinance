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


