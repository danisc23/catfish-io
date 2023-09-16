from pydantic import BaseModel


class User(BaseModel):
    id: str
    picture: str
    display_name: str
    email: str
    provider: str
