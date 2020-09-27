from django.test import TestCase
from sure import expect

from prime.utils.math import prime_sieve, fragment_prime_sieve


class PrimeSieveTestCase(TestCase):
    def test_prime_sieve(self):
        expect(prime_sieve(0)).to.be.empty
        expect(prime_sieve(1)).to.be.empty
        expect(prime_sieve(2)).to.be.empty
        expect(prime_sieve(3)).to.equal([2])
        expect(prime_sieve(4)).to.equal([2, 3])
        expect(prime_sieve(5)).to.equal([2, 3])
        expect(prime_sieve(6)).to.equal([2, 3, 5])
        expect(prime_sieve(7)).to.equal([2, 3, 5])
        expect(prime_sieve(10)).to.equal([2, 3, 5, 7])
        expect(prime_sieve(16)).to.equal([2, 3, 5, 7, 11, 13])

    def test_fragment_prime_sieve(self):
        # expect(fragment_prime_sieve(4, [2])).to.equal([3])
        # expect(fragment_prime_sieve(16, [2, 3, 5])).to.equal([7, 11, 13])
        expect(fragment_prime_sieve(100, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])).to.equal([
           37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
        ])
