import requests
import time
from logger_config import api_client

class APIclient:
    def __init__(self, base_url, headers=None, timeout=10):
        self.base_url = base_url
        self.headers = headers
        self.timeout = timeout

    def _request(self, method, endpoint, **kwargs):
        url = self.base_url + endpoint
        if self.headers:
            kwargs['headers'] = self.headers
        kwargs['timeout'] = self.timeout
        api_client.info(f"sending {method} to {url}")
        response = requests.request(method, url, **kwargs)
        if response.status_code >= 400:
            return None 
        else:
            return response

    def get_with_retry(self, endpoint, params=None, retries=3):
        for attempt in range(retries):
            try:
                response = self.get(endpoint, params=params)
                if response is None:
                    return None
                if response.status_code != 500:
                    return response
            except requests.exceptions.RequestException:
                pass
            time.sleep(3)  
        return None

    def head(self, endpoint, **kwargs):
        return self._request("HEAD", endpoint, **kwargs)

    def get(self, endpoint, params=None):
        return self._request("GET", endpoint, params=params)

    def post(self, endpoint, data=None, json=None):
        return self._request("POST", endpoint, data=data, json=json)

    def put(self, endpoint, data=None, json=None):
        return self._request("PUT", endpoint, data=data, json=json)

    def delete(self, endpoint):
        return self._request("DELETE", endpoint)


client = APIclient("https://api.github.com")
api_client.info(f"Base URL: {client.base_url}")

resp = client.head("/users/octocat")
api_client.info(f"HEAD request to /users/octocat returned status code: {resp.status_code}")

response = client._request("GET", "/users/octocat")
api_client.info(f"GET request to /users/octocat returned status code: {response.status_code}")




