import requests
from .config import *


class ContainerRequest:
    def __init__(self):

        self.json_create = {
            "fk_bim": bim_pk_global
        }
        self.json_update = {
            "fk_bim": bim_pk_global2
        }

    def create_container(self, cont_header = headers):

        response = requests.post(
            MAIN_URL + CONTAINER_URL + ADD,
            json=self.json_create,
            headers=cont_header
        )
        return response

    def get_container(self, pk=container_pk_global, cont_header=headers):
        response = requests.get(
            MAIN_URL + CONTAINER_URL + GET,
            headers=cont_header,
            params={"pk": pk}
        )
        return response

    def update_container(self, pk, cont_header=headers):
        response = requests.put(
            MAIN_URL + CONTAINER_URL + UPDATE,
            json=self.json_update,
            headers=cont_header,
            params={"pk": pk}
        )
        return response

    def delete_container(self, pk, cont_header=headers):
        response = requests.delete(
            MAIN_URL + CONTAINER_URL + DELETE,
            headers=cont_header,
            params={"pk": pk}
        )
        return response

    def restore_container(self, pk, cont_header=headers):
        response = requests.put(
            MAIN_URL + CONTAINER_URL + RESTORE,
            headers=cont_header,
            params={"pk": pk}
        )
        return response