import os

from django.core.handlers.wsgi import WSGIHandler

from todo.wsgi import application


def test_wsgi_default_settings():
    assert 'todo.settings' == os.environ["DJANGO_SETTINGS_MODULE"]


def test_application_instace():
    assert isinstance(application, WSGIHandler)