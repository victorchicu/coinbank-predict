from flask import Flask, jsonify, request
from api import Cryptocompare
import os
import json
import pandas as pd
import datetime as dt

app = Flask(__name__)


@app.route('/test')
def prepare_datasets():
    for i in range(7, 0, -1):
        end_of_day = dt.datetime.combine(dt.datetime.today() - dt.timedelta(days=i),  dt.time(23, 59, 59))
        ts = int(end_of_day.timestamp())
        response = Cryptocompare.get_historical_data_of_the_day(symbol="BTC", end_of_day=ts)
        sub_data = response["Data"]["Data"]
        json_string = json.dumps(sub_data);
        df_series = pd.read_json(json_string)
        df_series.drop(["conversionType", "conversionSymbol"], axis=1, inplace=True)
        file_name = str(dt.datetime.fromtimestamp(ts).date()) + ".csv"
        output_file = os.path.join("/home/victor_chicu/IdeaProjects/crypto/crypto-predict/static", file_name)
        df_series.to_csv(output_file, index=False)
    return "OK"

if __name__ == '__main__':
    app.run()
