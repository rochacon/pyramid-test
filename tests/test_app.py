# coding: utf-8
from pyramid.testing import DummyRequest as Request

from app import health


def test_health_page():
    req = Request()
    response = health(req)
    assert response.status_code == 200
    assert response.body == "I'm alive!"

