#!/usr/bin/python3
"""This function finds the change given the coins
and the total"""


def makeChange(coins, total):
    """This function finds the change.

    Args:
        coins: A list of the coins
        total: The total to be reached

    Return:
        If total is 0, returns 0
        if no change is found, returns -1
        otherwise, it returns the change
    """
    change = 0
    coins = sorted(coins, reverse=True)

    if total == 0:
        return 0

    for i in range(len(coins)):
        change += total // coins[i]
        total = total % coins[i]

    if total == 0:
        return change
    return -1
