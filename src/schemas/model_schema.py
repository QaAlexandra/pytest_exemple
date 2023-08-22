from pydantic import BaseModel, Field, HttpUrl, EmailStr, UUID4
from typing import Optional
from datetime import datetime



class DataItem(BaseModel):
    data: Optional[dict]

class BasicModelScema(BaseModel):
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



class BimItem(BaseModel):
    pk: str
    fk_owner: str
    name: Optional[str]
    description: Optional[str]
    priority: Optional[int]
    type: Optional[str]
    date_create: datetime
    date_read: Optional[datetime]
    date_update: Optional[datetime]
    date_delete: Optional[datetime]
    data: dict | str
    active: bool

class FileCloudItem(BaseModel):

    pk: str
    fk_owner: str
    type: str
    date_create: datetime
    file_cloud_id: int
    date_update: Optional[str] = None
    date_delete: Optional[str] = None
    last_path: Optional[str] = None

class GetModelSchema(BaseModel):
    pk: UUID4
    fk_owner: UUID4
    date_create: datetime
    fk_bim: UUID4
    fk_file: Optional[UUID4] = None
    fk_file_cloud_user: UUID4
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[int] = None
    type: Optional[str] = None
    date_read: Optional[datetime] = None
    date_update: Optional[datetime] = None
    date_delete: Optional[datetime] = None
    data: Optional[dict]
    bim: BimItem
    file: None
    file_cloud_user: FileCloudItem
