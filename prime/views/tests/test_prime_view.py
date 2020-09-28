from django.urls import reverse
from rest_framework.test import APITestCase
from sure import expect


class PrimeViewTestCase(APITestCase):
    def get_prime(self, n):
        url = f"{reverse('prime:previous_prime_number')}?n={n}"
        return self.client.get(url).data

    def test_get_prime(self):
        expect(self.get_prime(100)).to.equal(97)
        expect(self.get_prime(1000)).to.equal(997)
        expect(self.get_prime(10)).to.equal(7)
