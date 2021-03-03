from django.urls import path
from .consumers import WSconsumer

ws_urlpatterns = [
    path('ws/room/', WSconsumer.as_asgi()),
]
