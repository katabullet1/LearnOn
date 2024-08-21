from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from chat import routing # This change

application = ProtocolTypeRouter({
# (http->django views is added by default)
'websocket': AuthMiddlewareStack(
    URLRouter(
        routing.websocket_urlpatterns   #This change
    )
  ),
})