#!/usr/bin/python3
"""Sieve of erastothenes"""


def isWinner(x, nums):
    """
    This function finds the winner.

    Sieve of erastothenes: finds the prime numbers from 1 to 100
    get_winner: finds the winner

    Return:
        Winnner
    """
    def sieve_of_eratosthenes(n):
        # Create a list of booleans to mark numbers as prime or not
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

        # Mark multiples of each prime number as not prime
        for current in range(2, int(n ** 0.5) + 1):
            if sieve[current]:
                for multiple in range(current * current, n + 1, current):
                    sieve[multiple] = False

        # Return a list of prime numbers
        return [num for num, is_prime in enumerate(sieve) if is_prime]

    def get_winner(n):
        primes = sieve_of_eratosthenes(n)
        total_primes = len(primes)
        if total_primes % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    # Calculate the winner for each round and keep track of the count
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = get_winner(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
