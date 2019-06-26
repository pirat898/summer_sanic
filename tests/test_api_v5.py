import pytest

from main import web_app


@pytest.mark.parametrize(('url', ), [
    ('/api/v5/users/3', ),
    ('/api/v5/users/3/', ),
])
def test_user_get_by_id_returns_200(url):
    res = web_app.test_client.get(url)
    request, response = res
    assert response.status == 200


def test_user_get_by_incorrect_id_returns_400():
    res = web_app.test_client.get('/api/v5/users/g')
    request, response = res
    assert response.status == 400


def test_incorrect_url_returns_404():
    res = web_app.test_client.get('/hello_world')
    request, response = res
    assert response.status == 404
