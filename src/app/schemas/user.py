from datetime import datetime
from enum import Enum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from ..core.schemas import PersistentDeletion, TimestampSchema, UUIDSchema


class UserRole_Internal(str, Enum):
    admin = "admin"
    member = "member"
    superuser = "superuser"


class UserRole(str, Enum):
    admin = "admin"
    member = "member"


class UserBase(BaseModel):
    firstname: Annotated[str, Field(min_length=2, max_length=35, examples=["User"])]
    lastname: Annotated[str, Field(min_length=2, max_length=35, examples=["Userson"])]
    email: Annotated[EmailStr, Field(examples=["user.userson@example.com"])]
    phone_number: str | None


class User(TimestampSchema, UserBase, UUIDSchema, PersistentDeletion):
    hashed_password: str
    is_admin: bool = False
    is_superuser: bool = False
    client_id: int | None = None


class UserRead(BaseModel):
    id: int

    name: Annotated[str, Field(min_length=2, max_length=70, examples=["User Userson"])]
    email: Annotated[EmailStr, Field(examples=["user.userson@example.com"])]
    phone_number: str | None
    role: UserRole_Internal
    client_id: int | None
    client_name: str | None
    created_at: datetime
    updated_at: datetime | None
    created_by: str | None
    updated_by: str | None


class UserRegister(UserBase):
    model_config = ConfigDict(extra="forbid")

    role: UserRole


class UserRegisterInternal(UserBase):
    created_by_user_id: int | None
    client_id: int | None
    is_admin: bool = False
    is_superuser: bool = False


class UserCreate(UserBase):
    model_config = ConfigDict(extra="forbid")

    password: Annotated[str, Field(pattern=r"^.{8,}|[0-9]+|[A-Z]+|[a-z]+|[^a-zA-Z0-9]+$", examples=["Str1ngst!"])]


class UserCreateInternal(UserBase):
    hashed_password: str
    created_by_user_id: int | None
    client_id: int | None
    is_admin: bool = False
    is_superuser: bool = False


class UserUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: Annotated[str | None, Field(min_length=2, max_length=30, examples=["User Userberg"], default=None)]
    username: Annotated[
        str | None, Field(min_length=2, max_length=20, pattern=r"^[a-z0-9]+$", examples=["userberg"], default=None)
    ]
    email: Annotated[EmailStr | None, Field(examples=["user.userberg@example.com"], default=None)]
    profile_image_url: Annotated[
        str | None,
        Field(
            pattern=r"^(https?|ftp)://[^\s/$.?#].[^\s]*$", examples=["https://www.profileimageurl.com"], default=None
        ),
    ]


class UserUpdateInternal(UserUpdate):
    updated_at: datetime


class UserTierUpdate(BaseModel):
    tier_id: int


class UserDelete(BaseModel):
    model_config = ConfigDict(extra="forbid")

    is_deleted: bool
    deleted_at: datetime


class UserRestoreDeleted(BaseModel):
    is_deleted: bool
