def translate(word: str) -> str:

    word = word.lower()
    vowels = ["a", "e", "i", "o", "u"]
    special_cases = ["xr", "yt"]

    # Rule 1: Words starting with a vowel sound
    if word[0] in vowels:
        return word + "ay"

    # Rule 2: Words starting with a consonant sound
    for i in range(1, len(word)):
        if word[i] in vowels:
            return word[i:] + word[:i] + "ay"

    # Rule 3: Words starting with a consonant followed by "qu"
    if word.startswith("qu"):
        return word[2:] + "uay"

    # Rule 4: Words with "y" after a consonant cluster or as the second letter
    if word[1] == "y":
        return word[2:] + word[:2] + "ay"

    # Default case: Add "ay" to the end
    return word + "ay"
