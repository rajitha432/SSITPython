import pytest


@pytest.fixture(scope="session")
def get_token():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer bd6648bc9827db267da725fab6f1c7332b77ec3cce9b99745e10118116c1568d'
    }
    yield headers

# scopes of fixture =>
# by default it will be method
# module => it will be executed once for module
# session => it will be executed once for session
# class => it will be executed for test class once
