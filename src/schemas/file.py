from pydantic import BaseModel
from typing import List, Dict
from pydantic.types import Optional

class StandardFile(BaseModel):
    pk: str
    fk_owner: str
    type: str
    date_create: str
    file_cloud_id: int
    date_update: Optional[str] = None
    date_delete: Optional[str] = None
    last_path: Optional[str] = None