"""Sintetizador: agrega todos os fragmentos extraídos em um briefing executivo."""

from anthropic import Anthropic
from loguru import logger

from app.core.config import settings

SYSTEM_PROMPT = """Você é um analista sênior de comunicação corporativa da FSB Holding.
Receberá um conjunto estruturado de dados sobre um executivo brasileiro e deve produzir
um briefing executivo de 3 parágrafos em português:

1. Posicionamento público e trajetória recente.
2. Temas que a pessoa defende e tom da presença na mídia.
3. Momentos-chave dos últimos 12 meses e implicações para relacionamento.

Tom: profissional, objetivo, sem adjetivação excessiva. Cite fontes quando relevante."""


def sintetizar(dados_consolidados: dict) -> str | None:
    """Gera o briefing executivo de 3 parágrafos."""
    logger.info("LLM: sintetizando briefing executivo")
    client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)

    # TODO: implementar chamada Claude com os dados consolidados
    return None
