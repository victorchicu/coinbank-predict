from flask import Flask
from api import Cryptocompare

app = Flask(__name__)


@app.route('/price/<symbol>/to/<fiat>')
def get_crypto_price(symbol, fiat):
    return Cryptocompare.get_symbol_price(symbol, fiat)


if __name__ == '__main__':
    app.run()
