import json


def main():
    data = {}
    with open("glyph.json") as outfile:
        data = json.load(outfile)


main()
