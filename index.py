
from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap5
from forex_python.converter import CurrencyRates,  CurrencyCodes
import requests

from flask import request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap5(app)
def get_currency_info():
    #check the documentation hoo to use forex python 
    cr = CurrencyRates()
    cc = CurrencyCodes()
    #to get all country code from the api, and the code are keys in the api dictionary
    endpoint = f'https://v6.exchangerate-api.com/v6/2f37f7d40f9163a5c0ba1c85/latest/USD'
    r = requests.get(endpoint)
    data = r.json()
    # Define a list of common currency codes
    list_of_currencies = list(data['conversion_rates'].keys())

    # Get  currencyinfo
    currency_info = {code: {'name': cc.get_currency_name(code), 'symbol': cc.get_symbol(code) }for code in list_of_currencies}
    return currency_info

@app.route('/')
def index():
    currency_info = get_currency_info()
    return render_template('index.html', currency_info=currency_info)