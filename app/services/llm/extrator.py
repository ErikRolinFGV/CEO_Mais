"""Extrator estruturado: texto bruto -> JSON validado por Pydantic.

Usa Claude Sonnet com tool_use para forçar schema.
"""

from anthropic import Anthropic
from loguru import logger
from pydantic import BaseModel, Field

from app.core.config import settings


class EntidadesExtraidas(BaseModel):
    eventos: list[str] = Field(default_factory=list)
    empresas_mencionadas: list[str] = Field(default_factory=list)
    pessoas_mencionadas: list[str] = Field(default_factory=list)
    valores_monetarios: list[str] = Field(default_factory=list)
    datas: list[str] = Field(default_factory=list)
    sentimento: float = 0.0  # -1 a +1
    temas: list[str] = Field(default_factory=list)


SYSTEM_PROMPT = """Você é um extrator estruturado de informações para o setor de comunicação corporativa brasileiro.
Receberá um texto sobre um executivo (perfil, artigo, post) e deve extrair entidades estruturadas.
Seja preciso. Em caso de dúvida, prefira omitir a inventar."""


def extrair(texto: str, contexto_pessoa: str) -> EntidadesExtraidas | None:
    """Chama Claude e retorna entidades estruturadas, ou None em caso de falha."""
    logger.info("LLM: extraindo entidades estruturadas")
    client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)

    # TODO: implementar chamada real com tool_use para forçar o schema EntidadesExtraidas
    # client.messages.create(model="claude-sonnet-4-6", ...)
    return None
