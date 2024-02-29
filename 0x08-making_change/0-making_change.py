#!/usr/bin/python3
"""
Making change
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total amount.

    Args:
        coins: A list of the values of the coins in possession.
        total: The total amount to be met.

    Returns:
        The fewest number of coins needed to meet the total amount.
        Returns -1 if the total cannot be met by any number of coins.

    Notes:
        If total is 0 or less, returns 0.
        The value of a coin will always be an integer greater than 0.
        It is assumed that there is an infinite number of each
        denomination of coin in the list.

    Complexity Analysis:
        Time Complexity: O(n), where n is the total amount.
        Space Complexity: O(1).
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order

    num_coins = 0
    remaining_total = total

    # Iterate through each coin value
    for coin in coins:
        if coin <= remaining_total:
            # Calculate the maximum number of coins of this denomination
            num_coin_denomination = remaining_total // coin
            # Update the remaining total
            remaining_total -= num_coin_denomination * coin
            # Update the total number of coins used
            num_coins += num_coin_denomination

        if remaining_total == 0:
            break

    # If the total amount cannot be made with the given coins, return -1
    if remaining_total != 0:
        return -1

    return num_coins


if __name__ == '__main__':
    # Test cases
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
