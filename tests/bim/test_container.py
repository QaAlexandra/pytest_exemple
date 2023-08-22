import requests

from src.baseclasses.bim_db import get_container_from_db
from src.baseclasses.response import Response
from src.schemas.container import StandardContainer, GetContainer
from src.request_functions.container_requests import ContainerRequest



def test_create_container(create_bim_container):
    """Test creating a container 201"""
    response = Response(create_bim_container)
    response.assert_status_code(201).assert_not_value("fk_bim", None).validate(StandardContainer)


def test_get_container():
    """Test getting a container 200"""
    r = ContainerRequest().get_container(pk=get_container_from_db())
    response = Response(r)
    response.assert_status_code(200).validate(GetContainer)


def test_update_container(update_bim_container):
    """test updating a container 200"""
    response = Response(update_bim_container)
    (response.assert_status_code(200).assert_not_value("date_update", None).assert_value("fk_bim", bim_pk_global2).
     validate(StandardContainer))


def test_delete_container(delete_bim_container):
    """test deleting a container 200"""
    response = Response(delete_bim_container)
    response.assert_status_code(200).assert_not_value("date_delete", None).validate(StandardContainer)


def test_restore_container(restore_bim_container):
    """Test restoring a container 200"""

    response = Response(restore_bim_container)
    response.assert_status_code(200).validate(StandardContainer)


def test_create_container_401():
    """Test creating a container 401"""
    r = ContainerRequest().create_container(cont_header={"Authorization": "invalid_token"})
    response = Response(r)
    response.assert_status_code(401)


def test_get_container_401():
    """Test getting a container 401"""
    response = ContainerRequest().get_container(cont_header={"Authorization": "invalid"})
    response = Response(response)
    response.assert_status_code(401)


def test_update_container_401():
    """Test updating a container 401"""
    response = ContainerRequest().update_container(cont_header={"Authorization": "invalid"}, pk=container_pk_global)
    response = Response(response)
    response.assert_status_code(401)


def test_delete_container_401():
    """Test deleting a container 401"""
    response = ContainerRequest().delete_container(cont_header={"Authorization": "invalid"}, pk=container_pk_global)
    response = Response(response)
    response.assert_status_code(401)


def test_restore_container_401():
    """Test restoring a container 401"""
    response = ContainerRequest().restore_container(cont_header={"Authorization": "invalid"}, pk=container_pk_global)
    response = Response(response)
    response.assert_status_code(401)
