"""Modelo Cargo: ponte Pessoa <-> Empresa com período e função."""

from datetime import date

from sqlalchemy import Boolean, Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class Cargo(Base):
    __tablename__ = "cargo"

    id: Mapped[int] = mapped_column(primary_key=True)
    pessoa_id: Mapped[int] = mapped_column(ForeignKey("pessoa.id", ondelete="CASCADE"), index=True)
    empresa_id: Mapped[int] = mapped_column(ForeignKey("empresa.id", ondelete="CASCADE"), index=True)
    funcao: Mapped[str] = mapped_column(String(255))
    inicio: Mapped[date | None] = mapped_column(Date, nullable=True)
    fim: Mapped[date | None] = mapped_column(Date, nullable=True)
    eh_atual: Mapped[bool] = mapped_column(Boolean, default=False)

    pessoa: Mapped["Pessoa"] = relationship(back_populates="cargos")  # type: ignore[name-defined]  # noqa: F821
    empresa: Mapped["Empresa"] = relationship()  # type: ignore[name-defined]  # noqa: F821
