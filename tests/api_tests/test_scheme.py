from src.baseclasses.bim_db import get_from_db
from src.baseclasses.response import Response
from src.request_functions.schema_request import SchemaRequest
from src.schemas.model_schema import BasicModelScema


def test_create_scheme(create_scheme):
    """Test create scheme"""
    response = Response(create_scheme)
    response.assert_status_code(201).validate(BasicModelScema)


def test_get_scheme():
    """Test get scheme"""
    response = SchemaRequest().get_scheme(pk=get_from_db("ps_2d_scheme"))
    response = Response(response)
    response.assert_status_code(200).validate(BasicModelScema)


def test_update_scheme(update_scheme):
    """Test update scheme"""
    response = Response(update_scheme)
    (response.assert_status_code(200).assert_value('fk_bim', SchemaRequest().update_json['fk_bim']).
     assert_value("fk_file_cloud_user", SchemaRequest().update_json["fk_file_cloud_user"])
     .assert_value('name', SchemaRequest().update_json['name']).
     assert_value('description', SchemaRequest().update_json['description']).
     validate(BasicModelScema))


def test_delete_scheme(delete_scheme):
    """Test delete scheme"""
    response = Response(delete_scheme)
    response.assert_status_code(200).assert_not_value("date_delete", None).validate(BasicModelScema)


def test_restore_scheme(restore_scheme):
    """"Test restore scheme"""
    response = Response(restore_scheme)
    response.assert_status_code(200).validate(BasicModelScema)


def test_create_scheme_401():
    """Test create scheme 401"""
    response = SchemaRequest().create_schema(scheme_headers={"Authorization": "invalid"})
    response = Response(response)
    response.assert_status_code(401)


def test_get_scheme_401(delete_scheme):
    """"Test get scheme 401"""
    response = SchemaRequest().get_scheme(pk="asdad", scheme_headers={"Authorization": "ivalid"})
    response = Response(response)
    response.assert_status_code(401)


def test_update_scheme_401():
    response = SchemaRequest().update_schema(scheme_headers={"Authorization": "ivalid"}, pk= "asdasddas")
    response = Response(response)
    response.assert_status_code(401)


def test_delete_scheme_401():
    response = SchemaRequest().delete_scheme(scheme_headers={"Authorization": "ivalid"}, pk="asdasdd")
    response = Response(response)
    response.assert_status_code(401)
