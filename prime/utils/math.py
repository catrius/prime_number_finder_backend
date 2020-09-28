import math


def fragment_prime_sieve(n, pre_generated_primes=None):
    if n <= 2:
        return []

    if n == 3:
        return [2]

    _pre_generated_primes = pre_generated_primes if pre_generated_primes else [2]
    largest_prime = pre_generated_primes[len(pre_generated_primes) - 1] if pre_generated_primes else 2
    offset = largest_prime + 1
    is_prime = [True] * (n - offset)

    for prime in _pre_generated_primes:
        for j in range(prime * prime, n, prime):
            if j >= offset:
                is_prime[j - offset] = False

    for i in range(largest_prime + 1, math.floor(math.sqrt(n)) + 1):
        if is_prime[i - offset]:
            for j in range(i * i, n, i):
                is_prime[j - offset] = False

    return [i + offset for i, p in enumerate(is_prime) if p is True]
