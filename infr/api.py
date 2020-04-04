import requests


def make_request(method, url, **kwargs):
    response = requests.request(method, url, **kwargs)
    return response.json()


def get_onliner_forecast():
    url = 'https://www.onliner.by/sdapi/pogoda/api/forecast'
    return make_request(method='GET', url=url)
