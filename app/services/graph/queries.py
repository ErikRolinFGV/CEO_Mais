"""Consultas de grafo via CTEs recursivas em Postgres."""

from sqlalchemy import text
from sqlalchemy.orm import Session


def vizinhos_em_profundidade(
    db: Session,
    pessoa_id: int,
    profundidade: int = 2,
    peso_minimo: int = 2,
) -> dict:
    """Retorna {'nodes': [...], 'edges': [...]} expandindo até `profundidade` saltos."""
    sql = text(
        """
        WITH RECURSIVE rede AS (
            SELECT pessoa_a_id AS a, pessoa_b_id AS b, tipo, peso, 1 AS nivel
            FROM relacao
            WHERE (pessoa_a_id = :raiz OR pessoa_b_id = :raiz)
              AND peso >= :peso_minimo

            UNION

            SELECT r.pessoa_a_id, r.pessoa_b_id, r.tipo, r.peso, rede.nivel + 1
            FROM relacao r
            JOIN rede ON (r.pessoa_a_id = rede.a OR r.pessoa_a_id = rede.b
                       OR r.pessoa_b_id = rede.a OR r.pessoa_b_id = rede.b)
            WHERE rede.nivel < :profundidade
              AND r.peso >= :peso_minimo
        )
        SELECT DISTINCT a, b, tipo, peso FROM rede;
        """
    )
    rows = db.execute(
        sql,
        {"raiz": pessoa_id, "profundidade": profundidade, "peso_minimo": peso_minimo},
    ).fetchall()

    nodes: set[int] = set()
    edges = []
    for a, b, tipo, peso in rows:
        nodes.update({a, b})
        edges.append({"source": a, "target": b, "tipo": tipo, "peso": peso})

    return {"nodes": [{"id": n} for n in nodes], "edges": edges}
