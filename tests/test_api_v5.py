import pytest
from sanic.testing import SanicTestClient


from main import web_app


@pytest.mark.asyncio
async def test_index_returns_200():
    res = web_app.test_client.get('/api/v5/users')
    print(f"res: {res}")
    request, response = res
    # request, response = await web_app.test_client.get('/api/v7/users')
    assert response.status == 200


# def test_index_returns_200():
#     request, response = SanicTestClient(web_app, port=None).get('/api/v7/users')
#     assert response.status == 200
