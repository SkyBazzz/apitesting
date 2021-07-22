import pydantic


class User(pydantic.BaseModel):

    user_id: int = pydantic.Field(alias='id')
    email: str = pydantic.Field(alias='email')
    first_name: str = pydantic.Field(alias='first_name')
    last_name: str = pydantic.Field(alias='last_name')
    avatar: str = pydantic.Field(alias='avatar')
