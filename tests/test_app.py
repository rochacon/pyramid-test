# coding: utf-8
from pymongo import MongoClient
from pyramid.testing import DummyRequest as Request

from app import db, get_obj, health, put_obj


def test_health_page():
    req = Request()
    response = health(req)
    assert response.status_code == 200
    assert response.body == "I'm alive!"


def test_insert_obj():
    db.objs.drop()

    request = Request()
    request.json = {"test": "OK"}
    response = put_obj(request)
    assert response.status_code == 201
    assert db.objs.count() == 1
    assert response.json == {'success': True, 'id': str(db.objs.find()[0]['_id'])}


def test_insert_failure():
    pass
    # return Response(json.dumps({'error': 'Not created'}), status=500)


def test_get_obj():
    db.objs.drop()
    _id = db.objs.insert({'test': True})

    request = Request()
    response = get_obj(request, str(_id))
    assert response.status_code == 200
    assert response.json == {'test': True}


def test_get_obj_not_found():
    db.objs.drop()

    request = Request()
    response = get_obj(request, '0' * 24)
    assert response.status_code == 404
    assert response.body == ''
