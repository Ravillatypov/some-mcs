from typing import Tuple

from repositories.pg_models import PGWidget
from repositories.users.entities import User
from repositories.users.repo import get_user
from repositories.pg_widget.repo import upsert


async def create_widget(user_id: int, meta: dict) -> Tuple[User, PGWidget]:
    """Business logics for create wodget."""
    user = await get_user(user_id)
    # do something to check permission, ...
    widget = await upsert(user.currency_id, meta)

    return user, widget
