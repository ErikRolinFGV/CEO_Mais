"""POST /busca — entrada do fluxo de coleta sobre um executivo."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.schemas.busca import BuscaRequest, BuscaResponse

router = APIRouter(prefix="/busca", tags=["busca"])


@router.post("", response_model=BuscaResponse)
def criar_busca(req: BuscaRequest, db: Session = Depends(get_db)) -> BuscaResponse:
    """Cria ou recupera o perfil de um executivo.

    Fluxo (a ser implementado):
    1. Normaliza o nome em slug canônico.
    2. Verifica cache: se Pessoa existe e foi atualizada nos últimos N dias, retorna direto.
    3. Caso contrário, cria JobColeta e enfileira no Redis (RQ).
    4. Retorna job_id para o cliente acompanhar.
    """
    # TODO: implementar
    return BuscaResponse(
        cache_hit=False,
        mensagem=f"Stub: coleta de '{req.nome}' ainda não implementada.",
    )
