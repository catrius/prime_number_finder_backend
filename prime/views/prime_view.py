from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from prime.models import Prime


class PrimeView(APIView):
    def get(self, request):
        n = self.request.query_params.get('n', None)
        if not n:
            raise NotFound()
        return Response(Prime.previous_prime_large_number(int(n)), HTTP_200_OK)
