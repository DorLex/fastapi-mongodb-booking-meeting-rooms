from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

auth_router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)


@auth_router.post('/basic/')
async def login_basic(
        form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm)
):
    """Авторизация по логину и паролю"""

    return form_data.username
