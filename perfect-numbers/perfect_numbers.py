def classify(number: int) -> str:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    classification = ""
    divisors = []
    # add all the divisors
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)

    if sum(divisors) == number:
        return "perfect"
    elif sum(divisors) > number:
        return "abundant"
    else:
        return "deficient"
