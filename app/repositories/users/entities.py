from uuid import UUID

from pydantic.dataclasses import dataclass


@dataclass
class User:
    user_id: int
    email: str
    first_name: str
    last_name: str
    currency_id: UUID
