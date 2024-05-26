def is_isogram(string: str) -> bool:

    str_to_list: list[str] = list(string.lower().strip())

    seen_chars: set[str] = set()

    for char in str_to_list:
        if char in seen_chars:
            return False
        seen_chars.add(char)
    return True
