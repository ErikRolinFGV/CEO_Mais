"""Modelos SQLAlchemy. Importar todos aqui para o Alembic detectá-los."""

from app.models.cargo import Cargo
from app.models.empresa import Empresa
from app.models.evento import Evento
from app.models.job import JobColeta
from app.models.mencao import Mencao
from app.models.pessoa import Pessoa
from app.models.relacao import Relacao

__all__ = [
    "Cargo",
    "Empresa",
    "Evento",
    "JobColeta",
    "Mencao",
    "Pessoa",
    "Relacao",
]
