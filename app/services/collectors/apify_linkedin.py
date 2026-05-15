"""Coletor LinkedIn via Apify.

Actor recomendado: apimaestro/linkedin-profile-scraper
Docs: https://apify.com/apimaestro/linkedin-profile-scraper
"""

from apify_client import ApifyClient
from loguru import logger

from app.core.config import settings


def coletar_perfil_linkedin(linkedin_url: str) -> dict | None:
    """Dispara o actor do Apify e retorna o JSON bruto do perfil.

    Retorna None em caso de falha (perfil privado, actor sem créditos, etc.).
    """
    logger.info(f"Apify: coletando {linkedin_url}")
    client = ApifyClient(settings.APIFY_TOKEN)

    # TODO: ajustar nome do actor conforme o que estiver disponível na conta
    actor_id = "apimaestro/linkedin-profile-scraper"
    run_input = {"profileUrls": [linkedin_url]}

    try:
        run = client.actor(actor_id).call(run_input=run_input)
        items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
        return items[0] if items else None
    except Exception as exc:
        logger.error(f"Apify falhou para {linkedin_url}: {exc}")
        return None
