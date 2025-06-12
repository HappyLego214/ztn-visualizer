from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class UserBaseSchema(BaseModel):
    username: str
    email: str

class UserCreate(UserBaseSchema):
    password: str

class UserRead(UserBaseSchema):
    userID: str
    createdAt: datetime
    updatedAt: datetime
    active: bool

    class Config:
        orm_mode = True

class UserUpdate(UserBaseSchema):
    username: str | None = None
    email: str | None = None
    active: bool | None = None

class APITokenBaseSchema(BaseModel):
    label: str
    active: bool

class APITokenCreate(APITokenBaseSchema):
    pass

class APITokenRead(BaseModel):
    tokenID: UUID
    userID: UUID
    active: bool
    createdAt: datetime
    updatedAt: datetime
    lastUse: datetime | None

    class Config:
        orm_mode = True

class APITokenUpdate(APITokenBaseSchema):
    label: str | None = None
    active: bool | None = None

class SyncNetworkSchema(BaseModel):
    networkID: UUID
    tokenID: UUID
    label: str 
    accessControl: bool
    createdAt: datetime
    updatedAt: datetime
    active: bool

class SyncNetworkRead(BaseModel):
    label: str
    accessControl: bool
    active: bool

class SyncNetworkUpdate(BaseModel):
    label: str | None = None
    accessControl: bool | None = None
    active: bool | None = None 

class SyncDevice(BaseModel):
    deviceID: UUID
    networkID: UUID
    authorized: bool
    address: str
    label: str
    version: str
    managedIP: str
    createdAt: datetime
    updatedAt: datetime
    lastSeen: datetime | None
    active: bool

class SyncDeviceRead(BaseModel):
    deviceID: UUID
    networkID: UUID
    authorized: bool
    address: str
    label: str
    version: str
    managedIP: str
    lastSeen: datetime
    active: bool

class SyncDeviceUpdate(BaseModel):
    address: str | None = None
    label: str | None = None
    active: bool | None = None

