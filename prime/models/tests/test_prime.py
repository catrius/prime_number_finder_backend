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
        expect(Prime.previous_prime(19)).to.equal(17)
        expect(Prime.previous_prime(2)).to.equal(None)

        expect(Prime.objects.count()).to.equal(8)
        expect(Prime.previous_prime(24)).to.equal(23)
        expect(Prime.objects.count()).to.equal(9)

        expect(Prime.previous_prime(100)).to.equal(97)
        expect(Prime.objects.count()).to.equal(25)

        expect(Prime.previous_prime(90)).to.equal(89)
        expect(Prime.objects.count()).to.equal(25)

        expect(Prime.previous_prime(101)).to.equal(97)
        expect(Prime.objects.count()).to.equal(25)

        expect(Prime.previous_prime(1000000)).to.equal(999983)

    def test_previous_prime_large_number(self):
        expect(Prime.previous_prime_large_number(10000000)).to.equal(9999991)
