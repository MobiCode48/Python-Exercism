"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number: int) -> list:
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    list = []
    list.append(number)
    list.append(number + 1)
    list.append(number + 2)

    return list


def concatenate_rounds(rounds_1: list, rounds_2: list) -> list:
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds: list, number: int) -> bool:
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return True if number in rounds else False


def card_average(hand: list) -> float:
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand: list) -> bool:
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    first_elem, last_elem = hand[0], hand[-1]
    middle_value = hand[len(hand) // 2]

    avg_first_last = (first_elem + last_elem) / 2

    return avg_first_last == card_average(hand) or middle_value == card_average(hand)


def average_even_is_average_odd(hand: list) -> bool:
    """
    Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    # Initialize sums for even and odd indexed cards
    # Use list comprehension to separate even and odd indexed cards
    even_indices = [hand[i] for i in range(len(hand)) if i % 2 == 0]
    odd_indices = [hand[i] for i in range(len(hand)) if i % 2 != 0]

    # Calculate averages
    avg_even = sum(even_indices) / len(even_indices) if even_indices else 0
    avg_odd = sum(odd_indices) / len(odd_indices) if odd_indices else 0

    return avg_even == avg_odd


def maybe_double_last(hand: list) -> list:
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = 11 * 2
    return hand
