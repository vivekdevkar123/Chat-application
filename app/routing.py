from django.urls import path
from .consumers import *

websocket_urlpattern = [
    path('ws/sc/<str:groupname>/',MySyncConsumer.as_asgi()),
    path('ws/ac/<str:groupname>/',MyAsyncConsumer.as_asgi()),
]

# ws://127.0.0.1:8000/ws/sc/
# ws://127.0.0.1:8000/ws/ac/