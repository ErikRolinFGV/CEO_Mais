"""Inferidor de relações: identifica vínculos entre pessoas com base em contexto."""

from anthropic import Anthropic
from loguru import logger
from pydantic import BaseModel

from app.core.config import settings


class RelacaoInferida(BaseModel):
    pessoa_a: str
    pessoa_b: str
    tipo: str  # "co_evento", "co_board", "concorrente", "parceiro", etc.
    forca: int  # 1 a 5
    evidencia: str


def inferir(pessoa_alvo: str, contexto: list[dict]) -> list[RelacaoInferida]:
    """Para uma pessoa alvo e seu contexto, infere relações com outras pessoas.

    Cada item de `contexto` deve conter pelo menos `{texto, fonte, data}`.
    """
    logger.info(f"LLM: inferindo relações para '{pessoa_alvo}'")
    client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)

    # TODO: implementar com tool_use forçando lista de RelacaoInferida
    return []
