"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = None
SUPERLIST = None
EQUAL = None
UNEQUAL = None


def sublist(list_one: list, list_two: list):

    if list_one == list_two:
        return EQUAL

    if len(list_one) < len(list_two):
        return UNEQUAL

    if list_one == list_two[: len(list_one)]:
        return SUBLIST

    if list_one[: len(list_two)] == list_two:
        return SUPERLIST
