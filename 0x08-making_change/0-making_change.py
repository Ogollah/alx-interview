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
        Time Complexity: O(total * len(coins))
        Space Complexity: O(total)
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make a total of 0

    # Iterate through each coin value
    for coin in coins:
        # Update dp array for each possible total amount
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If the total amount cannot be made with the given coins, return -1
    if dp[total] == float('inf'):
        return -1

    return dp[total]


if __name__ == '__main__':
    # Test cases
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
