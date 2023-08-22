import requests
from tests.api_tests.config import (bim_url_global, MODEL_URL, bim_pk_global, file_pk_global,
                              bim_pk_global2, file_pk_global2, headers)

class ModelRequest:

    def __init__(self, fk_bim=bim_pk_global, fk_file=file_pk_global2):

        self.create_json = {
            "fk_bim": fk_bim,
            "fk_file_cloud_user": fk_file,
            "name": "Название 3d модели",
            "description": "Описание Описание",
            "priority": 1,
            "type": "тип1",
            "data": {
                "погода": "хорошая",
                "массив": ["значений"]
            }
        }
        self.update_json = {
            "fk_bim": bim_pk_global2,
            "fk_file_cloud_user": file_pk_global2,
            "name": "name name name name",
            "description": "description description description description",
            "priority": 111,
            "type": "type",
            "data": {  "погода": "хорошая" }
        }



    def create_model(self, model_headers = headers):
        resp = requests.post(
            url=bim_url_global + MODEL_URL + "/add",
            headers=model_headers,
            json= self.create_json)

        return resp


    def update_model(self, pk, model_headers=headers):
        resp = requests.put(
            url=bim_url_global + MODEL_URL + "/update",
            headers=model_headers,
            params={"pk": pk},
            json=self.update_json
        )
        return resp

    def delete_model(self, pk, model_headers = headers):
        resp = requests.delete(
            url=bim_url_global + MODEL_URL + "/delete",
            headers=model_headers,
            params={"pk": pk}
        )
        return resp


    def get_model(self, pk, model_headers = headers):

        resp = requests.get(
            url=bim_url_global + MODEL_URL + "/get_one",
            headers=model_headers,
            params={"pk": pk}
        )
        return resp

    def restore_model(self, pk, model_headers = headers):
        resp = requests.put(
            url=bim_url_global + MODEL_URL + "/restore",
            headers=model_headers,
            params={"pk": pk}
        )
        return resp