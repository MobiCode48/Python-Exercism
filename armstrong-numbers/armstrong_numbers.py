def is_armstrong_number(number: int) -> bool:
    digits: list[int] = [int(n) for n in str(number)]
    armstrongNumberSum: int = 0
    for val in digits:
        armstrongNumberSum += pow(val, len(digits))
    if armstrongNumberSum == number:
        return True

    return False
