import pytest

from main import web_app


@pytest.mark.asyncio
async def test_index_returns_200():
    request, response = await web_app.test_client.get('/api/v7/users')
    assert response.status == 200
