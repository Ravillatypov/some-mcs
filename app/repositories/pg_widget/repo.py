from uuid import UUID

from repositories.pg_models import PGWidget


async def upsert(currency_id: UUID, meta: dict) -> PGWidget:
    """Create new instance of PGWidget."""
    return await PGWidget.create(currency_id=currency_id, meta=meta)
