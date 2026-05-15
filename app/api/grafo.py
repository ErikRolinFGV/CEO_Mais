"""GET /grafo/{id} — retorna nós e arestas para visualização da rede de conexões."""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.db import get_db

router = APIRouter(prefix="/grafo", tags=["grafo"])


@router.get("/{pessoa_id}")
def obter_grafo(
    pessoa_id: int,
    profundidade: int = Query(2, ge=1, le=3),
    peso_minimo: int = Query(2, ge=1),
    db: Session = Depends(get_db),
) -> dict:
    """Retorna {'nodes': [...], 'edges': [...]} pronto para Cytoscape.js.

    Usa CTEs recursivas em Postgres para expandir a partir do nó raiz
    até `profundidade` saltos, filtrando arestas com peso >= peso_minimo.
    """
    # TODO: implementar consulta recursiva
    raise HTTPException(status_code=501, detail="Endpoint ainda não implementado")
