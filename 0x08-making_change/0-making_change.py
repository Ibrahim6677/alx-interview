#!/usr/bin/python3
"""
Module 0-making_change
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total.
    Optimized Dynamic Programming Bottom-Up Solution
    """
    if total <= 0:
        return 0

    # initialize list with a high value (total + 1 can't be reached)
    dp = [float('inf')] * (total + 1)
    # base case: 0 coins to make 0 total
    dp[0] = 0

    # iterate over every coin
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
