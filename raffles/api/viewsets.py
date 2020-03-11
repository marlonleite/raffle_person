import logging

import requests
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from requests import ReadTimeout, ConnectionError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import RaffleSerializer
from ..models import Raffle


@method_decorator(cache_page(60 * 2), name="list")
@method_decorator(vary_on_cookie, name="list")
class RaffleViewSet(ModelViewSet):
    """
    RaffleViewSet Api
    """
    queryset = Raffle.objects.all()
    serializer_class = RaffleSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    lookup_field = "number"


class RafflingAPIView(APIView):
    """
    RafflingAPIView Api
    """

    def get_object(self, number):
        try:
            return Raffle.objects.get(number=number)
        except Raffle.DoesNotExist:
            raise None

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, format=None):

        raffles = Raffle.objects.all()
        items = [item.number for item in raffles]

        try:

            url = f"{settings.SWEEPSTAKE_URL}/api/"
            response = requests.post(url, {"items": items})

            if response.status_code == 200:
                r = response.json()

                raffle = self.get_object(r["item"])

                if not raffle:
                    return Response({
                        "error": "Not found"
                    }, status=status.HTTP_404_NOT_FOUND)

                serializer = RaffleSerializer(instance=raffle)

                return Response(serializer.data, status=status.HTTP_200_OK)

        except (ConnectionError, ReadTimeout) as e:
            logging.error("Connection error")
            return Response({"error": "Connection error"},
                            status.HTTP_500_INTERNAL_SERVER_ERROR
                            )

        return Response({"error": "API Error."}, status=status.HTTP_400_BAD_REQUEST)
