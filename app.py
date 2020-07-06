import flask
from flask import Flask, request, render_template
import yfinance as yf


app = flask.Flask(__name__)
# app.config["DEBUG"] = True


# response status
def success(data):
    res = {}
    res['status'] = 200
    res['data'] = data
    return res


def error(message):
    return {'status': 300} if message is None else {'status': 300, 'message': message}


# routes
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# stock summary


@app.route('/info', methods=['GET'])
def info():
    symbol = request.args.get('symbol')

    if symbol is not None:
        return success(yf.Ticker(symbol).info)
    else:
        return error('Symbol not specified')

# option dates


@app.route('/options', methods=['GET'])
def options():
    symbol = request.args.get('symbol')

    if symbol is not None:
        return success(list(yf.Ticker(symbol).options))
    else:
        return error('Symbol not specified')

# option chain


@app.route('/optionchain', methods=['GET'])
def optionchain():
    symbol = request.args.get('symbol')
    date = request.args.get('date')

    def normalize_options(option, headers):
        normalized = {}

        for i, category in enumerate(option):
            normalized[headers[i]] = category

        return normalized

    if symbol and date:
        panda_df = yf.Ticker(symbol).option_chain(date)

        headers = list(panda_df[0])

        calls = panda_df[0].values.tolist()
        puts = panda_df[1].values.tolist()

        normalized_calls = [normalize_options(
            option, headers) for option in calls]
        normalized_puts = [normalize_options(
            option, headers) for option in puts]

        return success({'calls': normalized_calls, 'puts': normalized_puts})
    else:
        return error('Symbol or date not specified')


if __name__ == "main":
    app.run()

    # nodemon --exec flask run
