from django.db.models import Model, PositiveIntegerField, Max


class Prime(Model):
    prime = PositiveIntegerField()

    @classmethod
    def largest_prime(cls):
        query = cls.objects.all().aggregate(Max('prime'))
        return query['prime__max']

    @classmethod
    def primes(cls):
        return list(cls.objects.all().values_list('prime', flat=True))

    @classmethod
    def previous_prime(cls, n):
        query = cls.objects.filter(prime__lt=n)
        query = query.aggregate(Max('prime'))
        return query['prime__max']
