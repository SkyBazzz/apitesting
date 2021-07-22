import json
from json import JSONDecoder

import requests

from infrasctructure.logger import get_configured_logger


class Caller:
    LOG_TEMPLATE = 'Called {method}:{status_code}:{url}\nHeaders: {headers}\nUrlParams: {url_params}\nBody: {body}\n\nResponse: {response}'

    def __init__(self) -> None:
        self.logger = get_configured_logger('caller')
        self.session = requests.Session()
        self.headers = {
            'content-type': 'application/jons',
            'accept': 'application/json',
        }

    def call(self, method: str, url: str, url_params: dict = None, body: dict = None):
        body = body if body else {}
        url_params = self._clean_nones(url_params) if url_params else {}

        response: requests.Response = self.session.request(method=method, url=url, params=url_params, data=body,
                                                           headers=self.headers)
        try:
            response_to_log = json.dumps(json.loads(response.text), indent=4)
        except JSONDecoder:
            response_to_log = response.text
        self.logger.debug(self.LOG_TEMPLATE.format(method=method,
                                                   status_code=response.status_code
                                                   , url=url,
                                                   headers=response.headers,
                                                   url_params=url_params,
                                                   body=body,
                                                   response=response_to_log))

        if str(response.status_code).startswith('2'):
            return response
        else:
            raise ResponseError(f'Call failed with {response.status_code}')

    def _clean_nones(self, dict_obj: dict) -> dict:
        new_dict = {k: v for (k, v) in dict_obj.items() if v is not None}
        keys_to_remove = []
        for k in new_dict.keys():
            if isinstance(new_dict[k], dict):
                new_v = self._clean_nones(new_dict[k])
                if new_v:
                    new_dict[k] = new_v
                else:
                    keys_to_remove.append(k)
        [new_dict.pop(k) for k in keys_to_remove]
        return new_dict

class ResponseError(Exception):
    ...