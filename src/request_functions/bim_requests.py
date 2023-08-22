import requests

from .config import *
from src.baseclasses.bim_db import get_from_db


def get_one_bim(pk, bim_headers=headers):
    response = requests.get(MAIN_URL + BIM + GET, headers=bim_headers, params={"pk": pk})
    return response


class BimRequest:
    def __init__(self, get_all_params={"limit": 50, "offset": 0}):
        self.json_create = {
            "name": "test bim",
            "description": "1234 Description",
            "priority": 1,
            "type": "тип1",
            "data": {
                "siruation": "okey",
                "list": ["value1"]
            }
        }

        self.json_update = {
            "name": "test bim 2.0",
            "description": "123456 Description",
            "priority": 2,
            "type": "тип2",
            "data": {
                "siruation": "good",
                "list": ["value1", "value2"]
            }
        }
        self.get_all_params = get_all_params

    def create_bim(self, bim_headers=headers):
        response = requests.post(MAIN_URL + BIM + "/add", json=self.json_create, headers=bim_headers)
        return response

    def update_bim(self, pk, bim_headers=headers):
        response = requests.put(MAIN_URL + BIM + UPDATE, json=self.json_update,
                                headers=bim_headers, params={"pk": pk}, )
        return response

    def delete_bim(self, pk, bim_headers=headers):
        response = requests.delete(MAIN_URL + BIM + DELETE, headers=bim_headers, params={"pk": pk})
        return response

    def get_all_bims(self, bim_headers=headers):
        response = requests.get(MAIN_URL + BIM + GET_ALL, headers=bim_headers, params=self.get_all_params)
        return response

    def restore_bim(self, pk, bim_headers=headers):
        response = requests.put(MAIN_URL + BIM + RESTORE, headers=bim_headers, params={"pk": pk})
        return response
