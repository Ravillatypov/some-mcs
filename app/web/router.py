from fastapi import APIRouter, status, Depends
from entities.api.create import WidgetCreateRequest
from web.dependencies import get_user_id
from services.create import create_widget
from mappers.api.create import widget_created_mapper

router = APIRouter(prefix='/api/widget', tags=['widget'])


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_widget_http(
        request_model: WidgetCreateRequest,
        user_id: int = Depends(get_user_id),
):
    """Create widget."""
    user, widget = await create_widget(user_id, request_model.meta)
    return widget_created_mapper(user, widget)
