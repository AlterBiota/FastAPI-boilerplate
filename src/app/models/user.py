import uuid as uuid_pkg
from datetime import UTC, datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from ..core.db.database import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column("id", autoincrement=True, nullable=False, unique=True, primary_key=True, init=False)

    firstname: Mapped[str] = mapped_column(String(35))
    lastname: Mapped[str] = mapped_column(String(35))
    email: Mapped[str] = mapped_column(String(320), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    phone_number: Mapped[str] = mapped_column(String(15), nullable=True) # Find right type for pydantic verification

    uuid: Mapped[uuid_pkg.UUID] = mapped_column(default_factory=uuid_pkg.uuid4, primary_key=True, unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default_factory=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    created_by_user_id: Mapped[int | None] = mapped_column(Integer, nullable=True, default=None)
    updated_by_user_id: Mapped[int | None] = mapped_column(Integer, nullable=True, default=None)

    is_deleted: Mapped[bool] = mapped_column(default=False, index=True)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)

    is_superuser: Mapped[bool] = mapped_column(default=False)
    is_admin: Mapped[bool] = mapped_column(default=False)

    client_id: Mapped[int | None] = mapped_column(ForeignKey("client.id"), index=True, default=None, init=False)
