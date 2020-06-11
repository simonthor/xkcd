import requests

URL = "https://www.explainxkcd.com/wiki/api.php"

PARAMS = {
    "action": "parse",
    "page": "2311",
    "format": "json"
}

R = requests.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA["parse"]["text"]["*"])