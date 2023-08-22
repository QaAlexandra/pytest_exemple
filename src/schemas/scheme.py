from pydantic import BaseModel, Field, HttpUrl, EmailStr, UUID4
from typing import Optional
from datetime import datetime



class DataItem(BaseModel):
    data: Optional[dict]

class BasicSchema(BaseModel):
    data: DataItem
    pk: UUID4
    fk_owner: UUID4
    date_create: datetime
    fk_bim: Optional[UUID4] = None
    fk_file: Optional[UUID4] = None
    fk_file_cloud_user: Optional[UUID4] = None
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    type: Optional[str] = None
    date_read: Optional[datetime] = None
    date_update: Optional[datetime] = None
    date_delete: Optional[datetime] = None