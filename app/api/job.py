"""GET /job/{id} — status de uma coleta assíncrona."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.models.job import JobColeta

router = APIRouter(prefix="/job", tags=["job"])


@router.get("/{job_id}")
def status_job(job_id: int, db: Session = Depends(get_db)) -> dict:
    job = db.get(JobColeta, job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job não encontrado")
    return {
        "id": job.id,
        "termo_busca": job.termo_busca,
        "status": job.status,
        "pessoa_id": job.pessoa_id,
        "iniciado_em": job.iniciado_em.isoformat() if job.iniciado_em else None,
        "finalizado_em": job.finalizado_em.isoformat() if job.finalizado_em else None,
        "erro": job.erro,
    }
