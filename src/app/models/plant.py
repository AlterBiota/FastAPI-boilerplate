import uuid as uuid_pkg
from datetime import UTC, datetime

from sqlalchemy import DateTime, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from ..core.db.database import Base


class User_Plants_Permission(Base):
    __tablename__ = "user_plants_permission"

    id: Mapped[int] = mapped_column("id", autoincrement=True, nullable=False, unique=True, primary_key=True, init=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    plant_id: Mapped[int] = mapped_column(ForeignKey("plant.id"), index=True)
    permission: Mapped[str] = mapped_column(String, default="edit") # edit, view, none

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default_factory=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    is_deleted: Mapped[bool] = mapped_column(default=False, index=True)

    client_id: Mapped[int | None] = mapped_column(ForeignKey("client.id"), index=True, default=None, init=False)
    created_by_user_id: Mapped[int | None] = mapped_column(ForeignKey("user.id"), nullable=True, default=None, init=False)  # noqa: E501
    updated_by_user_id: Mapped[int | None] = mapped_column(ForeignKey("user.id"), nullable=True, default=None, init=False)  # noqa: E501


class Plant(Base):
    __tablename__ = "plant"

    id: Mapped[int] = mapped_column("id", autoincrement=True, nullable=False, unique=True, primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    description: Mapped[str] = mapped_column(String(100), nullable=True)

    uuid: Mapped[uuid_pkg.UUID] = mapped_column(default_factory=uuid_pkg.uuid4, primary_key=True, unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default_factory=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    is_deleted: Mapped[bool] = mapped_column(default=False, index=True)

    client_id: Mapped[int | None] = mapped_column(ForeignKey("client.id"), index=True, default=None, init=False)
    created_by_user_id: Mapped[int | None] = mapped_column(ForeignKey("user.id"), nullable=True, default=None, init=False)  # noqa: E501
    updated_by_user_id: Mapped[int | None] = mapped_column(ForeignKey("user.id"), nullable=True, default=None, init=False)  # noqa: E501
    deleted_by_user_id: Mapped[int | None] = mapped_column(ForeignKey("user.id"), nullable=True, default=None, init=False)  # noqa: E501

    UniqueConstraint('name', 'client_id', name='uix_plant_name_client_id')
