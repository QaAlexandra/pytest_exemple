from pydantic import BaseModel, EmailStr
from pydantic.types import Optional
from src.enums.user_enums import UserErrorsMSG, AuthErrorsMSG, EmailErrorsMSG


class Statuses(BaseModel):
    is_vendor: bool


# class Permissions(BaseModel):
#     storage_size: int
#     file_size: int

class AccessCloud(BaseModel):
    login: str
    password: str


class UserFullAnswer(BaseModel):
    """
Схема валидации при получении полной информации о юзере
    """
    pk: str
    email: EmailStr
    last_login: Optional[str]
    data: Optional[dict]
    is_active: Optional[bool]
    is_replaced_email: Optional[bool]
    date_create: str
    date_update: Optional[str]
    date_delete: Optional[str]
    statuses: Statuses
    subscription_end: Optional[str]
    access_cloud: Optional[AccessCloud]

    # permissions: Permissions
    # current_storage_size: float


class ShortAnswer(BaseModel):
    access_token: str
    refresh_token: str


class UserError(BaseModel):
    message: UserErrorsMSG

class UserPassError(BaseModel):
    password: Optional[AuthErrorsMSG]
    email: Optional[EmailErrorsMSG]

class Statuses(BaseModel):
    is_vendor: bool


class Permissions(BaseModel):
    storage_size: int
    file_size: int


class AccessCloudMassege(BaseModel):
    login: EmailStr
    password: str


class UpdatedUser(BaseModel):
    pk: str
    email: EmailStr
    last_login: Optional[str]
    data: Optional[dict]
    is_active: Optional[bool]
    is_emails_send: Optional[bool]
    is_replaced_email: Optional[bool]
    date_create: str
    date_update: str
    date_delete: Optional[str]

class WrongCredentials(BaseModel):

    email: Optional[str]
    password: Optional[str]

