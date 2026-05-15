"""Modelo Empresa."""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class Empresa(Base):
    __tablename__ = "empresa"

    id: Mapped[int] = mapped_column(primary_key=True)
    slug: Mapped[str] = mapped_column(String(160), unique=True, index=True)
    nome: Mapped[str] = mapped_column(String(255), index=True)
    setor: Mapped[str | None] = mapped_column(String(160), nullable=True)
    cnpj: Mapped[str | None] = mapped_column(String(20), nullable=True, index=True)
    ticker_b3: Mapped[str | None] = mapped_column(String(10), nullable=True)
    site: Mapped[str | None] = mapped_column(String(512), nullable=True)
