COLOUR_TO_CODE = {"absolutezero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff",
                "alizarincrimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00",
                "amethyst": "#9966cc", "antiquewhite": "#faebd7", "antiquewhite1": "#ffefdb",
                "apricot": "#fbceb1"}


colour = input("Enter colour name: ").lower()
while colour != "":
    try:
        print(colour, "is", COLOUR_TO_CODE[colour])
    except KeyError:
        print("Invalid colour name")
    colour = input("Enter colour name: ").lower()
