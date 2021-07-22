import pytest

from client.my_client import SampleClient
from infrasctructure.caller import ResponseError


class TestSample:

    @classmethod
    def setup_class(cls):
        cls.client = SampleClient()

    def test_smth(self):
        user = self.client.user_controller.get(2)
        print(user)

    def test_negative(self):
        with pytest.raises(ResponseError) as e :
            user = self.client.user_controller.get(-1)
            print(user)
        assert e.from_exc_info == 'error msg'