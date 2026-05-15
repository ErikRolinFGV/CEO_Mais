"""Worker que orquestra a coleta completa de um executivo.

Fluxo executado em segundo plano por RQ:
1. Atualiza JobColeta para "running".
2. Dispara coletores em sequência (LinkedIn, Crunchbase, SerpAPI, GDELT, B3, Receita).
3. Passa cada bloco de texto pelo extrator LLM.
4. Persiste Pessoa/Cargo/Empresa/Mencao/Evento.
5. Constrói/reforça arestas em Relacao a partir das pessoas co-mencionadas.
6. Chama sintetizador para gerar o briefing final.
7. Marca JobColeta como "done".
"""

from datetime import datetime, timezone

from loguru import logger
from sqlalchemy.orm import Session

from app.core.db import SessionLocal
from app.models.job import JobColeta, StatusJob


def executar_busca(job_id: int) -> None:
    """Entry point invocado pelo RQ."""
    db: Session = SessionLocal()
    try:
        job = db.get(JobColeta, job_id)
        if job is None:
            logger.error(f"Job {job_id} não encontrado")
            return

        job.status = StatusJob.RUNNING
        db.commit()
        logger.info(f"Job {job_id}: iniciando coleta de '{job.termo_busca}'")

        # TODO:
        # - chamar collectors em paralelo (asyncio ou threads)
        # - passar textos pelo extrator LLM
        # - persistir entidades
        # - reforçar relações no grafo
        # - chamar sintetizador

        job.status = StatusJob.DONE
        job.finalizado_em = datetime.now(timezone.utc)
        db.commit()
        logger.info(f"Job {job_id}: concluído")

    except Exception as exc:
        logger.exception(f"Job {job_id} falhou")
        if job is not None:
            job.status = StatusJob.FAILED
            job.erro = str(exc)
            job.finalizado_em = datetime.now(timezone.utc)
            db.commit()
    finally:
        db.close()
