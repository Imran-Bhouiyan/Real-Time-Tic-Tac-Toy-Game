from django.urls import path
from . import consumers

ws_urlpatterns = [
    path('ws/game/<room_code>', consumers.TicToyeAsync.as_asgi()),
    # path('ws/game/' , consumers.TicToyeAsync.as_asgi()),
]