from pydantic import BaseModel
from typing import List, Dict
from pydantic.types import Optional



class StandardBim(BaseModel):
    pk: str
    fk_owner: str
    name: Optional[str]
    description: Optional[str]
    priority: Optional[int]
    type: Optional[str]
    date_create: Optional[str]
    date_read: Optional[str]
    date_update: Optional[str]
    date_delete: Optional[str]
    data: Optional[dict]
    active: Optional[bool]




class StandardContainer(BaseModel):
    data: dict
    pk: str
    fk_product: Optional[str]
    fk_2d_scheme_element: Optional[str]
    fk_3d_model_element: Optional[str]
    fk_5d: Optional[str]
    fk_6d: Optional[str]
    fk_7d: Optional[str]
    fk_owner: str
    priority: None
    date_create: str
    date_read: Optional[str]
    date_update: Optional[str]
    date_delete: Optional[str]
    ports: dict | None


class DataItem(BaseModel):

    ver: float
    _2d: dict
    _3d: dict
    defaultProps: dict
    userProps: dict
    files: list[dict]
    props: list
    collisions: dict
    bim: Optional[StandardBim]
    ps_6d_mqtt: Optional[str]
    connection: Optional[list]
    ps_4d_task: Optional[list]


class GetContainer(BaseModel):


    pk: str
    fk_product: Optional[str]
    fk_2d_scheme_element: Optional[str]
    fk_3d_model_element: Optional[str]
    fk_5d: Optional[str]
    fk_6d: Optional[str]
    fk_7d: Optional[str]
    fk_owner: str
    priority: None
    date_create: str
    date_read: Optional[str]
    date_update: Optional[str]
    date_delete: Optional[str]
    data: DataItem