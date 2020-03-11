"""raffle_person URL Configuration

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('raffles.urls')),
]
