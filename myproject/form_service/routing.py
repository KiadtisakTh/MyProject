from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/form/', consumers.FormConsumer.as_asgi()),
]
