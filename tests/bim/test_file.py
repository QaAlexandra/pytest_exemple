import pytest
import requests

from src.baseclasses.response import Response
from src.schemas.file import StandardFile
from .config import *


def test_upload_file(upload_file):
    """Test upload file 201"""

    response = Response(upload_file)
    (response.assert_status_code(201).assert_not_value("file_cloud_id", None).
     assert_minimum_response_time(2).
     validate(StandardFile))


def test_get_file():
    """Test get file 200"""
    response = requests.get(
        url=bim_url_global + file_url + "/get_one",
        headers=headers,
        params={"pk_file": file_pk_global, "bim_pk": bim_pk_global2}
    )
    response = Response(response)
    response.assert_status_code(200).validate(StandardFile)


def test_download_file():
    """Download file_test and check size 200"""
    response = requests.get(
        url=bim_url_global + file_url + "/download_last_ver",
        headers=headers,
        params={"pk_file": file_pk_global3}
    )
    if response.status_code == 200:
        with open('скачанная-картинка.png', 'wb') as file_test:
            for chunk in response:
                file_test.write(chunk)

    im = Image.open('скачанная-картинка.png')
    width, height = im.size

    assert width == 652
    assert height == 531


def test_update_file():
    file = (os.path.dirname(__file__)) + "/новая-картинка.png"
    response = requests.put(
        url=bim_url_global + file_url + "/update_file",
        headers={"Authorization": "Bearer " + sing_in_and_get_token()},
        params={"pk_file": file_pk_global4, "bim_pk":bim_pk_global},
        files={"file": open(file, "rb")}
    )
    print(response.json())
    assert len(response.content) > 0
    assert response.status_code == 200
    assert response.json()["pk"] == file_pk_global4
    assert response.json()["date_update"] is not None


def test_download_file_update():
    response = requests.get(
        url=bim_url_global + file_url + "/download_last_ver",
        headers=headers,
        params={"pk_file": file_pk_global4, "bim_pk":bim_pk_global}
    )
    if response.status_code == 200:
        with open('скачанная-картинка-update.png', 'wb') as file_test:
            for chunk in response:
                file_test.write(chunk)

    im = Image.open('скачанная-картинка-update.png')
    width, height = im.size
    assert width == 708
    assert height == 232


# def test_get_prev_versions_file():
#     response = requests.get(
#         url=bim_url_global + file_url + "/get_prev_versions",
#         headers=headers,
#         params={"pk_file": file_pk_global3, "bim_pk": bim_pk_global}
#     )
#     pytest.file_prev_id = response.json()[0]["id_version"]
#     assert len(response.content) > 0
#     assert response.status_code == 200
#
#
# def test_download_prev_ver_file():
#     response = requests.get(
#         url=bim_url_global + file_url + "/download_prev_ver",
#         headers=headers,
#         params={"pk_file": file_pk_global3, "id_version": pytest.file_prev_id, "bim_pk": bim_pk_global}
#     )
#     if response.status_code == 200:
#         with open('скачанная-картинка-version.png', 'wb') as file:
#             for chunk in response:
#                 file.write(chunk)
#     im = Image.open('скачанная-картинка-version.png')
#     width, height = im.size
#     assert width == 652
#     assert height == 531


def test_delete_file(delete_file_in_api_and_restore):

    Response(delete_file_in_api_and_restore).assert_status_code(200).assert_not_value("date_delete",None).validate(StandardFile)



def test_download_file_delete(delete_file_in_api_and_restore):
    response = requests.get(
        url=bim_url_global + file_url + "/download_last_ver",
        headers=headers,
        params={"pk_file": file_pk_global4, "bim_pk": bim_pk_global}
    )
    Response(response).assert_status_code(404)


def test_restore_file(delete_file_in_api_and_restore_for_restore_test):

    Response(delete_file_in_api_and_restore_for_restore_test).assert_status_code(200).validate(StandardFile)
