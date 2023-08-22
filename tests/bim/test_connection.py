import pytest
import requests
from .config import bim_url_global
from .config import RequestDataConnection, headers, CONNECTION_URL
from src.schemas.coonection import StandardConnection
from src.baseclasses.response import Response


@pytest.mark.skip("issue 808")
def test_create_connection(create_connection):
    """Test create a connection 201"""
    response = Response(create_connection)
    response.assert_status_code(201).validate(StandardConnection)


@pytest.mark.skip("issue 808")
def test_delete_connection(create_connection):
    """Test delete a connection 200"""
    response = requests.delete(
        url=bim_url_global + CONNECTION_URL + "/delete",
        headers=headers,
        params={"pk": create_connection.json()["pk"]}
    )
    response = Response(response)
    response.assert_status_code(200).validate(StandardConnection)


@pytest.mark.skip("issue 808")
def test_restore_connection():
    """Test restore a connection 200"""
    response = requests.put(
        url=bim_url_global + CONNECTION_URL + "/restore",
        headers=headers,
        params={"pk": "*****"}
    )
    assert len(response.content) > 0
    assert response.status_code == 200
    assert response.json()["date_delete"] is None
