import json


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


def solve_for_i(p, r, t):
    return "%.2f" % (p*(r/100)*t)
