"""Coletor SerpAPI: Google search programático em portais brasileiros.

Docs: https://serpapi.com/search-api
"""

import httpx
from loguru import logger

from app.core.config import settings

PORTAIS_BR = [
    "valor.com.br",
    "estadao.com.br",
    "folha.uol.com.br",
    "exame.com",
    "infomoney.com.br",
    "neofeed.com.br",
    "brazilianreport.com",
]


def buscar_mencoes(nome: str, limite: int = 15) -> list[dict]:
    """Pesquisa o nome restrito aos principais portais BR e retorna resultados."""
    logger.info(f"SerpAPI: buscando menções de '{nome}'")
    site_filter = " OR ".join(f"site:{p}" for p in PORTAIS_BR)
    query = f'"{nome}" ({site_filter})'

    params = {
        "engine": "google",
        "q": query,
        "hl": "pt-br",
        "gl": "br",
        "num": limite,
        "api_key": settings.SERPAPI_KEY,
    }
    # TODO: chamar httpx.get("https://serpapi.com/search", params=params)
    return []
