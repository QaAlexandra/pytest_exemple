import pytest
from src.baseclasses.response import Response
from src.baseclasses.bim_db import get_from_db
from src.schemas.bim import StandardBim, GetBim, GetAllBim
from src.request_functions.bim_requests import BimRequest, get_one_bim
from .config import bim_pk_global

bim = "/api/bim"


def test_create_bim(create_bim):
    """Create item 201"""
    response = Response(create_bim)
    response.assert_status_code(201).validate(StandardBim)


def test_get_bim():
    """Get item and validate 200"""
    response = Response(get_one_bim(pk=get_from_db("bim")))
    response.assert_status_code(200).validate(GetBim)


def test_get_all_bim():
    """Get all items and validate 200"""
    r = BimRequest().get_all_bims()
    Response(r).assert_status_code(200).validate(GetAllBim)


def test_get_all_bim_order(create_bim):
    """Get all items and validate 200 with order by date_create ASC"""
    r = BimRequest(get_all_params={"limit": 50, "offset": 0, "order-by": "date_create ASC"}).get_all_bims()
    response = Response(r)
    (response.assert_status_code(200).assert_equal((r.json()["entries"][-1]["pk"]), create_bim.json()["pk"]).
     validate(GetAllBim))


def test_get_all_bim_deleted():
    """Get all items and validate 200 with deleted=true"""

    r = BimRequest(get_all_params={"limit": 50, "offset": 0, "deleted": "true"}).get_all_bims()
    Response(r).assert_status_code(200).validate(GetAllBim)


def test_update_bim(update_bim):
    """Update item and validate 200"""
    response = Response(update_bim)
    (response.assert_status_code(200).assert_value("description", BimRequest().json_update["description"]).
     assert_value("priority",BimRequest().json_update["priority"])
     .assert_value("type", BimRequest().json_update["type"]).validate(StandardBim))


def test_delete_bim(delete_bim):
    """Delete item and validate 200"""
    response = Response(delete_bim)
    response.assert_status_code(200).assert_not_value("date_delete", None).validate(StandardBim)

@pytest.mark.skip("issue 812")
def test_restore_bim(restore_bim):
    """Restore item and validate 200"""

    response = Response(restore_bim)

    response.assert_status_code(200).validate(StandardBim)



def test_create_bim_401():
    """Createitem with invalid token 401"""

    r = BimRequest().create_bim(bim_headers={"Authorization": "invalid"})
    Response(r).assert_status_code(401)


def test_get_bim_401():
    """Get item with invalid token 401"""
    r = get_one_bim(bim_headers={"Authorization": "invalid"}, pk=bim_pk_global)
    response = Response(r)
    response.assert_status_code(401)


def test_get_all_bim_401(delete_bim):
    """Get all items with invalid token 401"""
    r = BimRequest().get_all_bims(bim_headers={"Authorization": "invalid"})

    response = Response(r)
    response.assert_status_code(401)


def test_get_all_bim_409():
    """Get all items with query conflict 409"""
    r = BimRequest(get_all_params={"something":"else"}).get_all_bims()
    Response(r).assert_status_code(409)


def test_update_bim_401():
    """Update item with invalid token 401"""

    r = BimRequest().update_bim(bim_headers={"Authorization": "invalid"}, pk=bim_pk_global)
    response = Response(r)
    response.assert_status_code(401)

# "/add", "/update", "/delete", "/restore"
def test_delete_bim_401():
    """Delete item with invalid token 401"""
    r = BimRequest().delete_bim(bim_headers={"Authorization": "invalid"}, pk=bim_pk_global)
    response = Response(r)
    response.assert_status_code(401)


def test_restore_bim_401():
    """Restore item with invalid token 401"""
    r = BimRequest().restore_bim(bim_headers={"Authorization": "invalid"}, pk=bim_pk_global)
    response = Response(r)
    response.assert_status_code(401)
