from sqlalchemy import DateTime, ForeignKey, String, text
from uuid import UUID, uuid4
from sqlalchemy.orm import Mapped, Relationship, DeclarativeBase, mapped_column
from sqlalchemy.dialects.postgresql import INET
from datetime import datetime
from typing import Annotated

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    userID: Mapped[UUID] = mapped_column(primary_key=True, index=True, server_default=text("gen_random_uuid()"))
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    passwordHash: Mapped[str] = mapped_column(String(250), nullable=False)
    email: Mapped[str] = mapped_column(String(250), unique=True, nullable=False) 
    createdAt: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    updatedAt: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    active: Mapped[bool] = mapped_column(nullable=False)
    

class APITokens(Base):
    __tablename__ = "api_tokens"
    tokenID: Mapped[UUID] = mapped_column(primary_key=True, index=True, server_default=text("gen_random_uuid()"))
    userID: Mapped[UUID] = mapped_column(ForeignKey("users.userID"))
    tokenHash: Mapped[str] = mapped_column(String(250), nullable=False)
    label: Mapped[str] = mapped_column(String(100), nullable=True)
    createdAt: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    updatedAt: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    lastUse: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    active: Mapped[bool] = mapped_column(nullable=False)

class SyncNetworks(Base):
    __tablename__ = "sync_networks"
    networkID: Mapped[UUID] = mapped_column(primary_key=True, index=True, server_default=text("gen_random_uuid()"))
    tokenID: Mapped[UUID] = mapped_column(ForeignKey("api_tokens.tokenID"))
    label: Mapped[str] = mapped_column(String(100), nullable=True)
    accessControl: Mapped[bool] = mapped_column(server_default=text("false"), nullable=False),
    createdAt: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    updatedAt: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False) 
    active: Mapped[bool] = mapped_column(nullable=False)

class SyncDevices(Base):
    __tablename__= "sync_devices"
    deviceID: Mapped[UUID] = mapped_column(primary_key=True, index=True, server_default=text("gen_random_uuid()"))
    networkID: Mapped[UUID] = mapped_column(ForeignKey("sync_networks.networkID"))
    authorized: Mapped[bool] = mapped_column(server_default=text("false"), nullable=False)
    address: Mapped[str] = mapped_column(String(50), nullable=False)
    label: Mapped[str] = mapped_column(String(100), nullable=True)
    version: Mapped[str] = mapped_column(String(50), nullable=False)
    managedIP: Mapped[str] = mapped_column(nullable=False)
    createdAt: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    updatedAt: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    lastSeen: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    active: Mapped[bool] = mapped_column(nullable=False)

