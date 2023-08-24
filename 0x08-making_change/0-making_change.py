#!/usr/bin/python3

def makeChange(coins, total):
    change = 0
    coins = sorted(coins, reverse=True)

    if total == 0:
        return 0

    for i in range(len(coins)):
        change += total // coins[i]
        total = total % coins[i]

    if total == 0:
        return change
    else:
        return -1
