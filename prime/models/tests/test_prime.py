from django.test import TestCase
from sure import expect

from prime.factories import PrimeFactory
from prime.models import Prime


class PrimeTestCase(TestCase):
    def setUp(self):
        PrimeFactory(prime=2)
        PrimeFactory(prime=3)
        PrimeFactory(prime=5)
        PrimeFactory(prime=7)
        PrimeFactory(prime=11)
        PrimeFactory(prime=13)
        PrimeFactory(prime=17)
        PrimeFactory(prime=19)

    def test_largest_prime(self):
        expect(Prime.largest_prime()).to.equal(19)

    def test_primes(self):
        expect(Prime.primes()).to.equal([
            2, 3, 5, 7, 11, 13, 17, 19
        ])

    def test_previous_prime(self):
        expect(Prime.previous_prime(20)).to.equal(19)
        expect(Prime.previous_prime(19)).to.equal(17)
        expect(Prime.previous_prime(2)).to.equal(None)
