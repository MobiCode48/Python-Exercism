def value(colors: list) -> int | None:
    color_map = {
        "black": "0",
        "brown": "1",
        "red": "2",
        "orange": "3",
        "yellow": "4",
        "green": "5",
        "blue": "6",
        "violet": "7",
        "grey": "8",
        "white": "9",
    }
    val_cat = ""

    for color in colors:
        if color in color_map.keys():
            val_cat += color_map[color]

    return int(val_cat) if len(val_cat) == 2 else int(val_cat.replace(val_cat[-1], ""))


print(value(["blue", "grey"]))
