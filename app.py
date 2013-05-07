# coding: utf-8
from pyramid.config import Configurator
from pyramid.response import Response


def health(request):
    return Response('I\'m alive!')


# URLs
c = Configurator()
c.add_route('health', '/health')
c.add_view(health, route_name='health')

# health app
application = c.make_wsgi_app()

