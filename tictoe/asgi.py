import os

from channels.routing import ProtocolTypeRouter , URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tictac.settings')

# application = get_asgi_application()
import core.routing
django_asgi_app = get_asgi_application()



application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket':URLRouter(
        core.routing.ws_urlpatterns

    )
})

