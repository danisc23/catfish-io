from pydantic_factories import ModelFactory

from catfishio.core.auth.models import User


class UserFactory(ModelFactory):
    __model__ = User
