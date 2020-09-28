from django.db.models import Model, PositiveIntegerField

from prime.utils.math import fragment_prime_sieve


class Prime(Model):
    prime = PositiveIntegerField()

    class Meta:
        ordering = ['prime']

    @classmethod
    def largest_prime(cls):
        largest = cls.objects.last()
        if largest:
            return largest.prime

        Prime(prime=2).save()
        return 2

    @classmethod
    def primes(cls):
        return list(cls.objects.all().values_list('prime', flat=True))

    @classmethod
    def previous_prime(cls, n):
        largest_prime = cls.largest_prime()
        all_primes = cls.primes()
        new_primes = []

        if n <= 2:
            return None

        if n <= largest_prime:
            smaller_primes = [prime for prime in all_primes if prime < n]
            return smaller_primes[len(smaller_primes) - 1]

        if n - largest_prime >= 1000000:
            for current in range(largest_prime + 1, n, 1000000):
                current_new_primes = fragment_prime_sieve(current, pre_generated_primes=all_primes)
                new_primes.extend(current_new_primes)
                all_primes.extend(current_new_primes)

        current_new_primes = fragment_prime_sieve(n, pre_generated_primes=all_primes)
        new_primes.extend(current_new_primes)

        if not new_primes:
            return largest_prime

        new_primes_obj = [Prime(prime=prime) for prime in new_primes]
        Prime.objects.bulk_create(new_primes_obj)
        return new_primes[len(new_primes) - 1]
