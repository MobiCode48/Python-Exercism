def is_valid(isbn: str) -> bool:

    right_format = isbn.replace("-", "")
    sum_product = 0
    if len(right_format) != 10:
        return False

    for index in range(0, 11, -1):
        for char in list(right_format):
            if char.isdigit():
                value = 10 if char == "X" else int(char)
                sum_product += value * index

    return sum_product % 11 == 0


print(is_valid("3-598-21508-X"))
