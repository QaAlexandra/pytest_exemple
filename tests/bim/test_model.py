from src.baseclasses.bim_db import get_from_db
from src.baseclasses.response import Response
from src.request_functions.model_request import ModelRequest
from src.schemas.model_schema import BasicModelScema, GetModelSchema
from .config import RequestData, model_pk_global


def test_create_model(create_model):
    response = Response(create_model)
    response.assert_status_code(201).validate(BasicModelScema)


def test_get_model():
    resp = ModelRequest().get_model(pk=get_from_db('ps_3d_model'))
    (Response(resp)).assert_status_code(200).validate(GetModelSchema)


def test_update_model(update_model):
    (Response(update_model).assert_status_code(status_code=200).
     assert_value('fk_bim', RequestData.update_model['fk_bim']).
     assert_value("fk_file_cloud_user", RequestData.update_model["fk_file_cloud_user"]).
     assert_value('name', RequestData.update_model['name']).
     assert_value('description', RequestData.update_model['description']).validate(BasicModelScema))


def test_delete_model(create_and_delete_model):
    (Response(create_and_delete_model).assert_status_code(200).
     assert_not_value("date_create", None).validate(BasicModelScema))


def test_restore_model(restore_model):
    response = Response(restore_model)
    response.assert_status_code(200).assert_value("date_delete", None).validate(BasicModelScema)


def test_create_model_401():
    response = ModelRequest().create_model(model_headers={"Authorization": "dsfsfew"})
    response = Response(response)
    response.assert_status_code(401)


def test_create_model_404_bim():
    response = ModelRequest(fk_bim="ad4b5144-0000-0000-acd3-46204fa82ca4").create_model()
    Response(response).assert_status_code(404)


def test_create_model_404_file():
    response = ModelRequest(fk_file="ad4b5144-0000-0000-acd3-46204fa82ca4").create_model()
    Response(response).assert_status_code(404)


def test_get_model_401():
    response = ModelRequest().get_model(model_headers={"Authorization": "dsfsfew"}, pk=model_pk_global)
    Response(response).assert_status_code(401)


def test_update_model_401():
    response = ModelRequest().update_model(model_headers={"Authorization": "dsfsfew"}, pk=model_pk_global)
    Response(response).assert_status_code(401)


def test_model_404_bim_update():
    response = (ModelRequest(fk_bim="ad4b5144-0000-0000-acd3-46204fa82ca4").
                update_model(pk=model_pk_global))
    Response(response).assert_status_code(404)


def test_delete_model_401():
    response = ModelRequest().delete_model(model_headers={"Authorization": "dsfsfew"}, pk=model_pk_global)
    response = Response(response)
    response.assert_status_code(401)


def test_restore_model_401():
    response = ModelRequest().restore_model(model_headers={"Authorization": "dsfsfew"}, pk=model_pk_global)
    response = Response(response)
    response.assert_status_code(401)
