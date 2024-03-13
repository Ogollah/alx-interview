#!/usr/bin/python3
"""
Prime Game
"""


def generate_primes(n):
    """
    Generate a list of prime numbers up to a
    given number 'n' using the Sieve of Eratosthenes algorithm.

    Parameters:
    - n (int): The upper limit up to which to generate prime numbers.

    Returns:
    - list: A list of prime numbers up to 'n'.
    """
    primes = []
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False

    for p in range(2, n+1):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, n+1, p):
                sieve[i] = False

    return primes


def determine_winner(primes, player):
    """
    Determine the winner of a game round based on the
    list of prime numbers available and the current player.

    Parameters:
    - primes (list): A list of prime numbers available for selection.
    - player (int): The current player, either 1 (Ben) or 2 (Maria).

    Returns:
    - int or None: The winner of the game round
    (1 for Ben, 2 for Maria), or None if no winner.
    """
    for prime in primes:
        if prime <= player:
            return player
    return None


def isWinner(x, nums):
    """
    Determine the winner of multiple rounds of the prime game.

    Parameters:
    - x (int): The number of rounds to play.
    - nums (list): An array containing the upper limits 'n' for each round.

    Returns:
    - str or None: The name of the player who won the most rounds
    (either "Maria" or "Ben"),
    or None if the winner cannot be determined due to a tie.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = generate_primes(n)
        winner = determine_winner(primes, 2)
        if winner == 2:
            maria_wins += 1
        elif winner == 1:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
