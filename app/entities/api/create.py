from pydantic import BaseModel, Field


class WidgetCreateRequest(BaseModel):
    """Widget request model."""
    meta: dict = Field(alias='from_other_key')


class WidgetCreatedResponse(BaseModel):
    """Some fake response model."""
    user_name: str
    user_id: int
    meta: dict
