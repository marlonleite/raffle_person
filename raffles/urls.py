from django.urls import path, include
from rest_framework import routers

from raffles.api.viewsets import RaffleViewSet, RafflingAPIView

router = routers.DefaultRouter()

router.register(r'raffles', RaffleViewSet, basename="raffle")

urlpatterns = [
    path('', include(router.urls)),
    path('raffling/', RafflingAPIView.as_view(), name="raffling"),
]
