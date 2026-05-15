"""Modelo Evento: encontros públicos (Davos, Lide, etc.) com participantes."""

from datetime import date

from sqlalchemy import Column, Date, ForeignKey, Integer, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base

evento_participante = Table(
    "evento_participante",
    Base.metadata,
    Column("evento_id", Integer, ForeignKey("evento.id", ondelete="CASCADE"), primary_key=True),
    Column("pessoa_id", Integer, ForeignKey("pessoa.id", ondelete="CASCADE"), primary_key=True),
)


class Evento(Base):
    __tablename__ = "evento"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(255), index=True)
    tipo: Mapped[str | None] = mapped_column(String(80), nullable=True)
    data: Mapped[date | None] = mapped_column(Date, nullable=True)
    local: Mapped[str | None] = mapped_column(String(255), nullable=True)
    fonte_url: Mapped[str | None] = mapped_column(String(512), nullable=True)

    participantes: Mapped[list["Pessoa"]] = relationship(secondary=evento_participante)  # type: ignore[name-defined]  # noqa: F821
