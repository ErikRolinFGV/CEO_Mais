"""Schemas de request/response para o fluxo de busca."""

from pydantic import BaseModel, Field


class BuscaRequest(BaseModel):
    nome: str = Field(..., min_length=2, description="Nome do executivo a pesquisar")
    force_refresh: bool = Field(False, description="Ignora cache e recoleta tudo")


class BuscaResponse(BaseModel):
    job_id: int | None = None
    pessoa_id: int | None = None
    cache_hit: bool
    mensagem: str
