import uuid as uuid_pkg
from datetime import UTC, datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from ..core.db.database import Base


class Client(Base):
    __tablename__ = "client"

    id: Mapped[int] = mapped_column("id", autoincrement=True, nullable=False, unique=True, primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    initialization_date: Mapped[str] = mapped_column(DateTime(timezone=True), nullable=True)
    country: Mapped[str] = mapped_column(String(50), nullable=True)
    state_province: Mapped[str] = mapped_column(String(50), nullable=True)
    city: Mapped[str] = mapped_column(String(50), nullable=True)
    street: Mapped[str] = mapped_column(String(100), nullable=True)
    zip_code: Mapped[str] = mapped_column(String(10), nullable=True)
    unit: Mapped[str] = mapped_column(String(10), nullable=True) # Metric or Imperial
    standard_market: Mapped[str] = mapped_column(String(50), nullable=True) # ASTM, CSA, DIN, IS etc

    uuid: Mapped[uuid_pkg.UUID] = mapped_column(default_factory=uuid_pkg.uuid4, primary_key=True, unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default_factory=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), default=None)
    is_deleted: Mapped[bool] = mapped_column(default=False, index=True)

    tier_id: Mapped[int | None] = mapped_column(ForeignKey("tier.id"), index=True, default=None, init=False)

    # Client owner. Must be a user with admin role with the same client_id as the client
    owner_id: Mapped[int] = mapped_column(Integer, index=True, default=None, init=False)

    # Superuser. Must be a user with superuser role
    support_superuser_id: Mapped[int | None] = mapped_column(Integer, nullable=True, default=None, init=False)  # noqa: E501

    created_by_user_id: Mapped[int | None] = mapped_column(Integer, nullable=True, default=None)  # noqa: E501
    updated_by_user_id: Mapped[int | None] = mapped_column(Integer, nullable=True, default=None)  # noqa: E501
