from entities.api.create import WidgetCreatedResponse
from repositories.pg_models import PGWidget
from repositories.users.entities import User


def widget_created_mapper(user: User, widget: PGWidget) -> WidgetCreatedResponse:
    """Mapper for response."""
    return WidgetCreatedResponse(
        user_id=user.user_id,
        user_name=f'{user.first_name} {user.last_name}',
        meta=widget.meta,
    )
