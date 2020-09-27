from factory.django import DjangoModelFactory


class PrimeFactory(DjangoModelFactory):
    class Meta:
        model = 'prime.Prime'
