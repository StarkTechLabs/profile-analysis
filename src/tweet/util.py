import os

import requests

BASE_URL = "https://api.twitter.com/2"


def get_headers():
    appToken = os.environ["TWITTER_APP_TOKEN"] if "TWITTER_APP_TOKEN" in os.environ else ""
    if appToken is None or appToken == "":
        raise Exception("Missing env var 'TWITTER_APP_TOKEN' for twitter")

    return {
        "Authorization": "Bearer {appToken}".format(appToken=appToken)
    }


def get(path: str, params: object = {}):
    url = BASE_URL + path
    res = requests.get(url, params=params, headers=get_headers())
    if res.status_code >= 200 and res.status_code < 300:
        data = res.json()
        return {
            "data": data,
            "status_code": res.status_code,
            "ok": True
        }
    return {
        "error": res.text,
        "status_code": res.status_code,
        "ok": False
    }
