"""raffle_person URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Raffle Person API",
        default_version='v1',
        description="A simple sweepstake api to raffle person",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@dev.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include('raffles.urls')),
]
