from pydantic import EmailStr, BaseModel, ConfigDict


class UserBaseSchema(BaseModel):
    username: str
    email: EmailStr
    is_admin: bool


class UserOutSchema(UserBaseSchema):
    id: int

    model_config = ConfigDict(from_attributes=True)
