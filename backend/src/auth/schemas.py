from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class UserBaseSchema(BaseModel):
    email: str

class UserCreate(UserBaseSchema):
    hashed_password: str
    active: bool

class UserRead(UserBaseSchema):
    userID: UUID
    createdAt: datetime
    updatedAt: datetime
    active: bool

    class Config:
        orm_mode = True

class UserUpdate(UserBaseSchema):
    hashed_password: str | None = None
    email: str | None = None
    active: bool | None = None

class APITokenBaseSchema(BaseModel):
    label: str

class APITokenCreate(APITokenBaseSchema):
    pass

class APITokenRead(APITokenBaseSchema):
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
    label: str 

class SyncNetworkCreate(SyncNetworkSchema):
    pass

class SyncNetworkRead(SyncNetworkSchema):
    networkID: UUID
    tokenID: UUID
    accessControl: bool
    createdAt: datetime
    updatedAt: datetime
    active: bool

    class Config:
        orm_mode = True


class SyncNetworkUpdate(SyncNetworkSchema):
    label: str | None = None
    accessControl: bool | None = None
    active: bool | None = None 


class SyncDeviceSchema(BaseModel):
    label: str

class SyncDeviceRead(SyncDeviceSchema):
    deviceID: UUID
    networkID: UUID
    authorized: bool
    address: str
    version: str
    managedIP: str
    createdAt: datetime
    updatedAt: datetime
    lastSeen: datetime | None
    active: bool

    class Config:
        orm_mode = True


class SyncDeviceCreate(BaseModel):
    pass

class SyncDeviceUpdate(BaseModel):
    address: str | None = None
    label: str | None = None
    active: bool | None = None

