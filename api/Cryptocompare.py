import requests

API_KEY = "f01df1555a57232243f497f5fa31ab3ae984e45cc74c992e564ca79def08de4b"
BASE_URL = "https://min-api.cryptocompare.com"


def get_historical_data_of_the_day(symbol, end_of_day):
    url = BASE_URL + "/data/v2/histominute?fsym=" + symbol + "&tsym=USD" + "&limit=" + str(1440) + "&toTs=" + str(end_of_day) + "&api_key=" + API_KEY
    response = requests.get(url)
    return response.json()
