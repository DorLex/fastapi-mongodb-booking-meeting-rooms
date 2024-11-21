from fastapi import APIRouter, Depends

from src.apps.users.models import UserModel
from src.apps.users.schemas import UserOutSchema
from src.apps.users.services.auth import get_current_user

router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)


@router.post(
    '/basic',
    response_model=UserOutSchema
)
async def login_basic(
        current_user: UserModel = Depends(get_current_user)
):
    """Авторизация по логину и паролю"""

    return current_user
