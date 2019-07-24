import json


def main():
    data = {}
    with open("glyph.json") as outfile:
        data = json.load(outfile)



def solve_for_i(p, r, t):
    return "%.2f" % (p*(r/100)*t)
