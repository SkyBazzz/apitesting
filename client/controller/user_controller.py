import json

from client.controller.base_controller import BaseController
from entities.entities import User

from infrasctructure.caller import Caller
from schemas.get_user_schemas import get_user_scheme


class UserController(BaseController):
    POSTFIX = 'users'

    def __init__(self, caller: Caller) -> None:
        self.caller = caller

    def get(self, user_id) -> User:
        response = self.caller.call('get', url=f"{self.BASE_URL}{self.API_PREFIX}{self.POSTFIX}/{user_id}")
        user_info = json.loads(response.text)['data']
        get_user_scheme(user_info)
        return User.parse_obj(user_info)