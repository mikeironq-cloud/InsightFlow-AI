from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, String, Text, func
from sqlalchemy.dialects.postgresql import UUID as PostgreSQLUUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Feedback(Base):
    """Customer feedback submitted to InsightFlow AI."""

    __tablename__ = "feedback"

    id: Mapped[UUID] = mapped_column(
        PostgreSQLUUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    source: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    external_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    text: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    language: Mapped[str | None] = mapped_column(
        String(10),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
