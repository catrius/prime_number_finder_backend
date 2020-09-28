from django.test import TestCase
from sure import expect

from prime.utils.math import fragment_prime_sieve


class PrimeSieveTestCase(TestCase):
    def test_fragment_prime_sieve(self):
        expect(fragment_prime_sieve(2)).to.equal([])
        expect(fragment_prime_sieve(3)).to.equal([2])
        expect(fragment_prime_sieve(4, [2])).to.equal([3])
        expect(fragment_prime_sieve(16, [2, 3, 5])).to.equal([7, 11, 13])
        expect(fragment_prime_sieve(100, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])).to.equal([
           37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
        ])
