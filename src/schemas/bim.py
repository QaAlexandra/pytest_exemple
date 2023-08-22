from pydantic import BaseModel
from typing import List, Dict
from pydantic.types import Optional


class DataItemCreate(BaseModel):
    погода: str
    массив: List[str]


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
    data: dict | str
    active: Optional[bool]




class BimContainerItem(BaseModel):
    pk: str
    fk_product: Optional[str]
    fk_2d_scheme_element: Optional[str]
    fk_3d_model_element: Optional[str]
    fk_5d: Optional[str]
    fk_6d: Optional[str]
    fk_7d: Optional[str]
    fk_owner: str
    priority: None
    date_create: Optional[str]
    date_read: Optional[str]
    date_update: Optional[str]
    date_delete: Optional[str]
    ports: dict
    data: dict


class GetBim(BaseModel):
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
    bim_container: list[BimContainerItem]
    ps_2d_scheme:list
    ps_3d_model: list
    access:dict
    task: dict




class GetAllBim(BaseModel):
    total_count: int
    limit: int
    offset: int
    entries: list[StandardBim]