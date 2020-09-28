from django.db.models import Model, PositiveIntegerField, Max

from prime.utils.math import fragment_prime_sieve


class Prime(Model):
    prime = PositiveIntegerField()

    @classmethod
    def largest_prime(cls):
        query = cls.objects.all().aggregate(Max('prime'))
        if query['prime__max']:
            return query['prime__max']
        Prime(prime=2).save()
        return 2

    @classmethod
    def primes(cls):
        return list(cls.objects.all().values_list('prime', flat=True))

    @classmethod
    def previous_prime(cls, n):
        largest_prime = cls.largest_prime()
        if n <= cls.largest_prime():
            query = cls.objects.filter(prime__lt=n)
            query = query.aggregate(Max('prime'))
            return query['prime__max']
        else:
            new_primes=fragment_prime_sieve(n, pre_generated_primes=cls.primes())
            if new_primes:
                new_primes_obj = [Prime(prime=prime) for prime in new_primes]
                Prime.objects.bulk_create(new_primes_obj)
                return new_primes[len(new_primes) - 1]
            return largest_prime

    @classmethod
    def previous_prime_large_number(cls, n):
        largest_prime = cls.largest_prime()
        if n - largest_prime >= 1000000:
            for current in range(largest_prime + 1, n, 1000000):
                cls.previous_prime(current)

        return cls.previous_prime(n)
