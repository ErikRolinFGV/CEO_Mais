"""Coletor GDELT: eventos globais e menções na mídia internacional.

Docs: https://blog.gdeltproject.org/gdelt-doc-2-0-api-debuts/
API gratuita, sem autenticação.
"""

import httpx
from loguru import logger

GDELT_URL = "https://api.gdeltproject.org/api/v2/doc/doc"


def buscar_eventos(nome: str, dias: int = 90) -> list[dict]:
    """Retorna artigos GDELT mencionando o nome nos últimos `dias`."""
    logger.info(f"GDELT: buscando '{nome}' nos últimos {dias} dias")
    params = {
        "query": f'"{nome}"',
        "mode": "ArtList",
        "maxrecords": 50,
        "timespan": f"{dias}d",
        "format": "json",
    }
    # TODO: implementar httpx.get(GDELT_URL, params=params)
    return []
