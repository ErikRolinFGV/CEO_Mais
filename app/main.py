"""Entrypoint da aplicação FastAPI.

Rodar local:
    uvicorn app.main:app --reload
"""

from fastapi import FastAPI
from loguru import logger

from app.api import busca, grafo, job, perfil
from app.core.config import settings

app = FastAPI(
    title="FSB Executive Intelligence",
    description="Plataforma de inteligência sobre executivos brasileiros — MVP para FSB Holding.",
    version="0.1.0",
)

app.include_router(busca.router)
app.include_router(perfil.router)
app.include_router(grafo.router)
app.include_router(job.router)


@app.get("/", tags=["health"])
def health() -> dict:
    return {"status": "ok", "env": settings.APP_ENV, "version": app.version}


@app.on_event("startup")
def on_startup() -> None:
    logger.info(f"FSB Executive Intelligence iniciado em ambiente {settings.APP_ENV}")
