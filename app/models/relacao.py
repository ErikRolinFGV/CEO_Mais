"""Modelo Relacao: aresta Pessoa <-> Pessoa do grafo de conexões inferidas."""

from sqlalchemy import JSON, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class Relacao(Base):
    """Aresta direcionada A->B. Para relações simétricas garantir A<B por convenção."""

    __tablename__ = "relacao"
    __table_args__ = (
        UniqueConstraint("pessoa_a_id", "pessoa_b_id", "tipo", name="uq_relacao_tripla"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    pessoa_a_id: Mapped[int] = mapped_column(ForeignKey("pessoa.id", ondelete="CASCADE"), index=True)
    pessoa_b_id: Mapped[int] = mapped_column(ForeignKey("pessoa.id", ondelete="CASCADE"), index=True)

    # Ex: "co_mencionado", "co_evento", "co_board", "cliente_fornecedor"
    tipo: Mapped[str] = mapped_column(String(60))
    peso: Mapped[int] = mapped_column(Integer, default=1)

    # Lista de IDs/URLs que comprovam a relação (mencao_id, evento_id, url, etc.)
    evidencias: Mapped[list[dict]] = mapped_column(JSON, default=list)
