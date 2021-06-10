import requests
import json

from requests.exceptions import RequestException
from json.decoder import JSONDecodeError

class __requests_handler:

    def __init__(self):
        pass

    def request_get(self, url, headers, params):
        try:
            response = requests.get(url, headers = headers, params = params)
        except RequestException:
            raise
        try:
            response.raise_for_status()
            content = json.loads(response.content.decode('utf-8'))
            return content
        except Exception as e:
            # Check if JSON (with error messages) is returned
            try:
                content = json.loads(response.content.decode('utf-8'))
                raise valueError(content)
            # If no JSON
            except JSONDecodeError:
                pass
            raise
    
    def request_post(self, url, headers, params):
        try:
            response = requests.post(url, headers = headers, parmas = params)
        except RequestException:
            raise
        try:
            response.raise_for_status()
            content = json.loads(response.content.decode('utf-8'))
            return content
        except Exception as e:
            try:
                content = json.loads(response.content.decode('utf-8'))
                raise valueError(content)
            # If no JSON
            except JSONDecodeError:
                pass
            
            raise