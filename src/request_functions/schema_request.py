import requests
from .config import *

class SchemaRequest:
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

    def create_schema(self, scheme_headers = headers):
        response = requests.post(MAIN_URL + SCHEME_URL + ADD, json=self.create_json, headers=scheme_headers)
        return response

    def update_schema(self, pk, scheme_headers = headers, ):
        response = requests.put(MAIN_URL + SCHEME_URL + UPDATE, json=self.update_json,
                                headers=scheme_headers, params={"pk": pk})
        return response

    def get_scheme(self, pk, scheme_headers = headers):
        response = requests.get(MAIN_URL + SCHEME_URL + GET, headers=scheme_headers, params={"pk": pk})
        return response

    def delete_scheme(self, pk, scheme_headers = headers):
        response = requests.delete(MAIN_URL + SCHEME_URL + DELETE, headers=scheme_headers, params={"pk": pk})
        return response

    def restore_scheme(self, pk, scheme_headers=headers):
        response = requests.put(MAIN_URL + SCHEME_URL + RESTORE, headers=scheme_headers, params={"pk": pk})
        return response