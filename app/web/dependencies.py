from fastapi import Depends
from fastapi.security import APIKeyHeader

from settings import setting

auth_token = APIKeyHeader(name='Authorization', scheme_name='Bearer', description='JWT auth')


def get_user_id(access_token: str = Depends(auth_token)) -> int:
    """Get user ID from jwt token."""
    if not setting.auth.is_enabled or access_token is setting.auth.service_token:
        return setting.auth.fake_user_id
    # get payload from token and return user ID
