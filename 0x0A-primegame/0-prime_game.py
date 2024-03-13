#!/usr/bin/python3
"""
Prime Game
"""


def is_prime(n):
    """ Check if n is a prime number """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def add_primes(n, primes):
    """ Add prime numbers up to n to the list """
    last_prime = primes[-1]
    if n > last_prime:
        for i in range(last_prime + 1, n + 1):
            if is_prime(i):
                primes.append(i)
            else:
                primes.append(0)


def determine_winner(num_rounds, nums):
    """
    Determine the winner based on the number of
    rounds and the given array of nums
    """
    scores = {"Maria": 0, "Ben": 0}
    primes = [0, 0, 2]
    add_primes(max(nums), primes)

    for round_num in range(num_rounds):
        prime_count = sum(
            (i != 0 and i <= nums[round_num])
            for i in primes[:nums[round_num] + 1]
        )
        if prime_count % 2:
            winner = "Maria"
        else:
            winner = "Ben"
        scores[winner] += 1

    if scores["Maria"] > scores["Ben"]:
        return "Maria"
    elif scores["Ben"] > scores["Maria"]:
        return "Ben"

    return None
