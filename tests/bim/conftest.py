import pytest
import requests
from src.baseclasses.db_classes import delete_from_db
from src.request_functions.model_request import ModelRequest
from src.request_functions.bim_requests import BimRequest
from src.request_functions.container_requests import ContainerRequest
from src.request_functions.schema_request import SchemaRequest
from .config import *



@pytest.fixture()
def create_bim():
    resp = BimRequest().create_bim()
    yield resp
    delete_from_db('bim', resp.json()["pk"])

@pytest.fixture()
def update_bim(create_bim):
    resp = BimRequest().update_bim(create_bim.json()["pk"])
    yield resp


@pytest.fixture()
def delete_bim(create_bim):
    resp = BimRequest().delete_bim(create_bim.json()["pk"])
    yield resp

@pytest.fixture()
def restore_bim(delete_bim):
    resp = BimRequest().restore_bim(delete_bim.json()["pk"])
    yield resp

@pytest.fixture()
def create_bim_container():
    resp = ContainerRequest().create_container()
    yield resp
    delete_from_db('bim_container', resp.json()["pk"])

@pytest.fixture()
def update_bim_container(create_bim_container):
    resp = ContainerRequest().update_container(create_bim_container.json()["pk"])
    yield resp

@pytest.fixture()
def delete_bim_container(create_bim_container):
    resp = ContainerRequest().delete_container(create_bim_container.json()["pk"])
    yield resp


@pytest.fixture()
def restore_bim_container(delete_bim_container):
    resp = ContainerRequest().restore_container(delete_bim_container.json()["pk"])
    yield resp



### Create and delete test models
@pytest.fixture()
def create_model():
    resp = ModelRequest().create_model()
    yield resp
    delete_from_db('ps_3d_model', resp.json()["pk"])


@pytest.fixture()
def update_model(create_model):
    resp = ModelRequest().update_model(create_model.json()["pk"])
    yield resp


@pytest.fixture()
def create_and_delete_model(create_model):
    resp = ModelRequest().delete_model(create_model.json()["pk"])
    yield resp


@pytest.fixture()
def restore_model(create_and_delete_model):
    resp = ModelRequest().restore_model(create_and_delete_model.json()["pk"])
    return resp


@pytest.fixture()
def create_connection():
    resp = requests.post(
        url=bim_url_global + CONNECTION_URL + "/add",
        headers=headers,
        json=RequestDataConnection.data_create
    )
    yield resp
    delete_from_db('connection', resp.json()["pk"])

@pytest.fixture()
def create_scheme():
    resp = SchemaRequest().create_schema()
    yield resp
    delete_from_db('ps_2d_scheme', resp.json()["pk"])

@pytest.fixture()
def update_scheme(create_scheme):
    resp = SchemaRequest().update_schema(create_scheme.json()["pk"])
    yield resp

@pytest.fixture()
def delete_scheme(create_scheme):
    resp = SchemaRequest().delete_scheme(create_scheme.json()["pk"])
    yield resp

@pytest.fixture()
def restore_scheme(delete_scheme):
    resp = SchemaRequest().restore_scheme(delete_scheme.json()["pk"])
    yield resp

@pytest.fixture()
def upload_file():
    r = requests.post(
        url=bim_url_global + file_url + "/upload",
        headers=headers,
        params=file_params,
        files={"file": open(file, "rb")}
    )
    yield r


@pytest.fixture()
def delete_file_in_api_and_restore():
    """Fixture to delete a file from the API and restore it back to the database."""
    response = requests.delete(
        url=bim_url_global + file_url + "/delete",
        headers=headers,
        params={"pk": file_pk_global4, "bim_pk": bim_pk_global}
    )
    yield response
    requests.put(
        url=bim_url_global + file_url + "/restore",
        headers=headers,
        params={"pk": file_pk_global4, "bim_pk": bim_pk_global}
    )

@pytest.fixture()
def delete_file_in_api_and_restore_for_restore_test():
    response = requests.delete(
        url=bim_url_global + file_url + "/delete",
        headers=headers,
        params={"pk": file_pk_global4, "bim_pk": bim_pk_global}
    )
    requests.put(
        url=bim_url_global + file_url + "/restore",
        headers=headers,
        params={"pk": file_pk_global4, "bim_pk": bim_pk_global}
    )
    yield response




