
from flask import Flask, render_template, flash, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from forex_python.converter import CurrencyRates,  CurrencyCodes
import requests

from flask import request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap5(app)
api_key = '2f37f7d40f9163a5c0ba1c85'

def get_currency_info():
    #check the documentation hoo to use forex python 
    cr = CurrencyRates()
    cc = CurrencyCodes()
    #to get all country codes from the api, and the codes are keys in the api dictionary
    endpoint = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'
    r = requests.get(endpoint)
    data = r.json()
    # Define a list of common currency codes
    list_of_currencies = list(data['conversion_rates'].keys())

    # Get  currencyinfo
    currency_info = {code: {'name': cc.get_currency_name(code), 'symbol': cc.get_symbol(code) }for code in list_of_currencies}
    return currency_info
searched = False

@app.route('/rates', methods=['POST'])
def rates():
    from_currency = request.form.get('currencyCode')

    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}'
    
    response = requests.get(url)
    data = response.json()
    
    if data['result'] == 'success':
        selected_currency_symbol = None
        sorted_currency_rate_info = sorted(data['conversion_rates'].items(), key=lambda item: item[1])
        for currency_code, info in get_currency_info().items():
            if currency_code == from_currency:
                selected_currency_symbol = info['symbol']
                break

        if selected_currency_symbol is None:
            # Handle the case where the symbol is not found
            flash(f'Symbol for the selected currency code {selected_currency} not found.', 'error')
            
        return render_template(
            'rates.html', 
            currency_rate_info=data['conversion_rates'], 
            last_updated=data['time_last_update_utc'], 
            selected_currency=from_currency,
            selected_currency_symbol = selected_currency_symbol
        )
    else:
        # Handle error or unsuccessful response
        flash('There was a problem retrieving the exchange rates.', 'error')
        return redirect(url_for('exchangeRates'))

def generate_plot():
    # No plot for now, return an empty string
    return ''

@app.route('/')
def index():
    plot_html = generate_plot()
    return render_template('index.html', plot_html=plot_html)

@app.route('/countryCodes')
def countryCodes():
    global searched
    searched = False  # Reset the flag when loading the main table
    currency_info = get_currency_info()
    return render_template('countryCodes.html', currency_info=currency_info, searched=searched)

@app.route('/search', methods=['POST'])
def search():
    global searched
    searched = True

    search_term = request.form.get('search_term', '').lower()

    currency_info = get_currency_info()
    filtered_currency_info = {}
    for code, info in currency_info.items():
        if (code is not None and search_term in code.lower()) or \
           (info['name'] is not None and search_term in info['name'].lower()):
            filtered_currency_info[code] = info

    if not filtered_currency_info:
        flash(f'Country "{search_term}" not found in the table.', 'error')

    return render_template('countryCodes.html', currency_info=filtered_currency_info, searched=searched)

@app.route('/exchangeRates')
def exchangeRates():
    currency_info = get_currency_info()
    return render_template('exchangeRates.html', currency_info=currency_info)