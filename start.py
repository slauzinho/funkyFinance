import json


def print_result(number_to_print):
    """
    Takes a string of numbers and prints the equivalent glyph.
    :param number_to_print: Number to be printed into a glyph.
    """
    data = {}
    glyphList = []
    with open("glyph.json") as outfile:
        data = json.load(outfile)

    for letter in number_to_print:
        glyphList.append(data[letter].split("\n"))
        glyphList.append(data[" "].split("\n"))

    print_glyphs(glyphList)


def print_glyphs(listOfLetters):
    """
    Prints into the screen the combination of a list of glyphs.
    :param listOfLetters: List of glyphs to be printed
    """
    for row in list(zip(*listOfLetters)):
        text = ""
        for letter in row:
            text = text + letter
        print(text)


def solve_for_i(p, r, t):
    return "%.2f" % (p*(r/100)*t)
