from todo.api.apps import ApiConfig


def test_api():
    assert ApiConfig.name == 'api'