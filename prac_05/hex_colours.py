"""CP1404-practical 5
dictionary program to look up hexadecimal colour codes
"""

AVAILABLE_COLOURS = {"ABSOLUTE ZERO": "#0048ba",
                     "ALICE BLUE": "#f0f8ff",
                     "AMETHYST": "#9966cc",
                     "ASPARAGUS": "#87a96b",
                     "BAKER MILLER PINK": "#ff91af",
                     "BARN RED": "#7c0a02",
                     "BEAVER": "#9f8170",
                     "BITTER LEMON": "#bfff00",
                     "BLACK": "#000000",
                     "BLUE BELL": "#a2a2d0"}

colour_name = input("Pick a colour name: ").strip().upper()
while colour_name != "":
    if colour_name in AVAILABLE_COLOURS:
        print(colour_name, "is", AVAILABLE_COLOURS[colour_name])
    else:
        print("Invalid colour choice!")
    colour_name = input("Pick a colour name: ").strip().upper()
