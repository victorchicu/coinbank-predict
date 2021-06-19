import requests

API_KEY = "f01df1555a57232243f497f5fa31ab3ae984e45cc74c992e564ca79def08de4b"
BASE_URL = "https://min-api.cryptocompare.com/data"


def get_symbol_price(symbol, fiat):
    url = BASE_URL + "/price?fsym=" + symbol + "&tsyms=" + fiat + "&api_key" + API_KEY;
    response = requests.get(url)
    return response.json()
