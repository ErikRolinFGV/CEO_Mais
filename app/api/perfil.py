"""GET /perfil/{id} — retorna o dossiê completo de uma pessoa."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.db import get_db

router = APIRouter(prefix="/perfil", tags=["perfil"])


@router.get("/{pessoa_id}")
def obter_perfil(pessoa_id: int, db: Session = Depends(get_db)) -> dict:
    """Retorna pessoa, cargos, mencoes recentes e briefing executivo.

    A implementação real deve montar um dict com:
      - dados básicos da Pessoa
      - cargos (atuais e históricos)
      - menções (ordenadas por data desc)
      - eventos
      - briefing (texto sintetizado pelo LLM)
    """
    # TODO: implementar
    raise HTTPException(status_code=501, detail="Endpoint ainda não implementado")
