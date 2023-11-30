from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap5
from forex_python.converter import CurrencyRates,  CurrencyCodes
from pycountry_convert import country_alpha2_to_continent_code, country_name_to_country_alpha2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap5(app)
def get_currency_info():
    cr = CurrencyRates()
    cc = CurrencyCodes()


    # Define a list of common currency codes
    list_of_currencies = ["USD", "GBP", "ILS", "DKK", "CAD", "IDR", "BGN",
    "JPY", "HUF", "RON", "MYR", "SEK", "SGD", "HKD", "AUD", "CHF", "KRW", "CNY", "TRY", "HRK", "NZD", "THB", "LTL", "NOK", "RUB",
    "INR", "MXN", "CZK", "BRL", "PLN", "PHP", "ZAR"]



    # Get country names
    currency_info = {code: {'name': cc.get_currency_name(code), 'symbol': cc.get_symbol(code), 'rates' :cr.get_rates(code) }for code in list_of_currencies}
    return currency_info

@app.route('/')
def index():
    currency_info = get_currency_info()
    return render_template('index.html', currency_info=currency_info)

