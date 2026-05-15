"""Coletor Receita Federal / CNPJ: quadros societários.

Fontes possíveis: cnpj.ws, brasilapi.com.br, cnpja.com
"""

import httpx
from loguru import logger


def buscar_socios_por_nome(nome: str) -> list[dict]:
    """Retorna empresas onde a pessoa figura como sócia ou administradora."""
    logger.info(f"Receita: cruzando quadro societário de '{nome}'")
    # TODO: definir provedor (cnpj.ws tem free tier, brasilapi é totalmente grátis)
    return []
