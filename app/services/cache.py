"""Cache de buscas em Redis (TTL configurável)."""

import json
from datetime import timedelta

import redis
from loguru import logger

from app.core.config import settings

_client: redis.Redis | None = None


def get_redis() -> redis.Redis:
    global _client
    if _client is None:
        _client = redis.from_url(settings.REDIS_URL, decode_responses=True)
    return _client


def get_busca(termo: str) -> dict | None:
    """Retorna resultado cacheado de uma busca, ou None."""
    chave = f"busca:{termo.lower()}"
    raw = get_redis().get(chave)
    return json.loads(raw) if raw else None


def set_busca(termo: str, payload: dict) -> None:
    chave = f"busca:{termo.lower()}"
    ttl = timedelta(days=settings.CACHE_TTL_DAYS)
    get_redis().setex(chave, ttl, json.dumps(payload, default=str))
    logger.debug(f"Cache set: {chave} (TTL {ttl})")
