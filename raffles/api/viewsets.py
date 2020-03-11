import requests
from django.conf import settings
from requests import ReadTimeout, ConnectionError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import RaffleSerializer
from ..models import Raffle


class RaffleViewSet(ModelViewSet):
    """
    RaffleViewSet Api
    """
    queryset = Raffle.objects.all()
    serializer_class = RaffleSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    lookup_field = "number"



