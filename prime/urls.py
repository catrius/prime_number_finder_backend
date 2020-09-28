from django.urls import path

from prime.views.prime_view import PrimeView

urlpatterns = [
    path('', PrimeView.as_view(), name='previous_prime_number'),
]
