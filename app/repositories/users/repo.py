from .entities import User


async def get_user(user_id: int) -> User:
    """Get user from users service via HTTP."""
