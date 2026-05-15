"""Coletor Crunchbase: carreira corporativa, board memberships, M&A.

Docs: https://data.crunchbase.com/docs
"""

import httpx
from loguru import logger

from app.core.config import settings

BASE_URL = "https://api.crunchbase.com/api/v4"


def buscar_pessoa(nome: str) -> dict | None:
    """Procura pessoa por nome e retorna o registro mais relevante."""
    logger.info(f"Crunchbase: buscando '{nome}'")
    # TODO: implementar chamada real ao endpoint /searches/people
    return None


def obter_pessoa(uuid: str) -> dict | None:
    """Retorna detalhes completos de uma pessoa por UUID Crunchbase."""
    # TODO: implementar chamada ao endpoint /entities/people/{uuid}
    return None
