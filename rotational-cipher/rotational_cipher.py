import string


def rotate(text: str, key: int) -> str:
    cipher = ""
    for character in text:

        if character not in string.punctuation or not character.isdigit():
            ascii_value = ord(character)  # get the ascii value
            ascii_shifted_value = ascii_value + key  # perform the shift
        else:
            cipher += character

        if character.islower():
            if ascii_shifted_value < ord("a"):
                ascii_shifted_value += 26
            elif ascii_shifted_value > ord("z"):
                ascii_shifted_value -= 26
        else:
            if ascii_shifted_value < ord("A"):
                ascii_shifted_value += 26
            elif ascii_shifted_value > ord("Z"):
                ascii_shifted_value -= 26

        cipher += chr(ascii_shifted_value)

    print(cipher)
    return cipher


def rotate(text, key):
    newtext = ""
    for c in text:
        if c.isalpha():
            if c.isupper():
                newtext += chr(((ord(c) - 65 + key) % 26) + 65)  ## 65 == ord('A')
            else:
                newtext += chr(((ord(c) - 97 + key) % 26) + 97)  ## 97 == ord('a')
        else:
            newtext += c
    return newtext


print(rotate("omg", 5))
