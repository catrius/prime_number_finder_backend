from django.urls import reverse
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.test import APITestCase
from sure import expect


class PrimeViewTestCase(APITestCase):
    def get_prime(self, n):
        url = f"{reverse('prime:previous_prime_number')}?n={n}"
        return self.client.get(url)

    def test_get_prime(self):
        expect(self.get_prime(100).data).to.equal(97)
        expect(self.get_prime(1000).data).to.equal(997)
        expect(self.get_prime(10).data).to.equal(7)
        expect(self.get_prime(-1).data).to.be.none

    def test_get_prime_failed(self):
        expect(self.get_prime('abc').status_code).to.equal(HTTP_404_NOT_FOUND)
        expect(self.client.get(f"{reverse('prime:previous_prime_number')}").status_code).to.equal(HTTP_404_NOT_FOUND)
