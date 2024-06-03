def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:

    if input_base < 2:
        raise ValueError("input_base and output_base must be >= 2")

    if output_base < 2:
        raise ValueError("input_base and output_base must be >= 2")

    if all(d < 0 for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    if all(d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    if output_base == 10:
        return [int(d) for d in digits]

    return [
        int(d)
        for d in [
            str(d)
            for d in [
                sum([input_base**i * digit for i, digit in enumerate(digits[::-1])])
                for input_base in range(output_base)
            ]
        ]
    ]
