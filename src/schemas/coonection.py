from pydantic import BaseModel
from typing import List, Dict
from pydantic.types import Optional


class StandardConnection(BaseModel):
    pk: str
    fk_container_1: str
    fk_container_2: str
    fk_owner: str
    port_1: Optional[int]
    port_2: Optional[str]
    date_create: str
    date_read: Optional[str]
    date_update: Optional[str]
    date_delete: Optional[str]
    data: dict | str
