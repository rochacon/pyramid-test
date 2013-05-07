# coding: utf-8
import json

from bson.objectid import ObjectId
from pymongo import MongoClient
from pyramid.config import Configurator
from pyramid.response import Response


mongo = MongoClient()
db = mongo.tumblelog


def get_obj(request, _id):
    obj = db.objs.find_one({'_id': ObjectId(_id)})
    if obj:
        return Response(json.dumps(obj))
    return Response(status=404)


def put_obj(request):
    id = db.objs.insert(request.json)
    if id:
        return Response(json.dumps({'success': True, 'id': str(id)}), status=201)
    return Response(json.dumps({'error': 'Not created'}), status=500)


def health(request):
    return Response('I\'m alive!')


# URLs
config = Configurator()
config.add_route('health', '/health')
config.add_view(health, route_name='health')
config.add_route('get', '/get', request_method=('get',))
config.add_view(get_obj, route_name='get')
config.add_route('put', '/put', request_method=('PUT',))
config.add_view(put_obj, route_name='put')

# health app
application = config.make_wsgi_app()


if __name__ == '__main__':
    import wsgiref.simple_server
    server = wsgiref.simple_server.make_server('127.0.0.1', 8000, application)
    server.serve_forever()
