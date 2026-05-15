"""Modelo Pessoa: executivo individual."""

from datetime import datetime

from sqlalchemy import DateTime, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class Pessoa(Base):
    __tablename__ = "pessoa"

    id: Mapped[int] = mapped_column(primary_key=True)
    slug: Mapped[str] = mapped_column(String(160), unique=True, index=True)
    nome: Mapped[str] = mapped_column(String(255), index=True)
    nome_completo: Mapped[str | None] = mapped_column(String(255), nullable=True)
    cargo_atual: Mapped[str | None] = mapped_column(String(255), nullable=True)
    bio: Mapped[str | None] = mapped_column(Text, nullable=True)
    linkedin_url: Mapped[str | None] = mapped_column(String(512), nullable=True)
    foto_url: Mapped[str | None] = mapped_column(String(512), nullable=True)

    # Briefing executivo gerado pelo sintetizador LLM
    briefing: Mapped[str | None] = mapped_column(Text, nullable=True)

    criado_em: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    atualizado_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    cargos: Mapped[list["Cargo"]] = relationship(back_populates="pessoa", cascade="all, delete-orphan")  # type: ignore[name-defined]  # noqa: F821
    mencoes: Mapped[list["Mencao"]] = relationship(back_populates="pessoa", cascade="all, delete-orphan")  # type: ignore[name-defined]  # noqa: F821
