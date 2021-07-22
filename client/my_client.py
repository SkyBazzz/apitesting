from client.controller.user_controller import UserController
from infrasctructure.caller import Caller


class SampleClient:
    def __init__(self) -> None:
        caller = Caller()
        self.user_controller = UserController(caller)