"""Coletor B3: comunicados ao mercado, transações de insiders e assembleias.

Fonte: https://www.rad.cvm.gov.br/ENET/
"""

from loguru import logger


def buscar_documentos_executivo(nome: str, ticker: str | None = None) -> list[dict]:
    """Retorna documentos CVM/B3 onde o executivo aparece."""
    logger.info(f"B3/CVM: buscando documentos de '{nome}'")
    # TODO: implementar scraping do portal RAD/CVM (Playwright)
    return []
