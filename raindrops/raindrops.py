def convert(number: int) -> str:
    converter = ""
    if number % 3 == 0:
        converter += "Pling"
    if number % 5 == 0:
        converter += "Plang"
    if number % 7 == 0:
        converter += "Plong"
    if not converter:
        return str(number)
    return converter
