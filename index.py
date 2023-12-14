'''
Course:CST205-01_FA23: Multimedia Design & Progmng
Title: Currency Exchanage Project
Abstract: The provided Python code is the backend component for our web application built using the Flask framework
Authors:Tamanna Zahir, Rakery Cheng, Delight Lee, and Haider Syed
Date: 12/11/23
Note: Who worked on which functions is listed above each function
'''
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

# This route handles POST requests when a user wants to view exchange rates from a specific currency to other currencies
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


@app.route('/')
def index():
    return render_template('index.html')

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

from forex_python.converter import RatesNotAvailableError

def get_exchange_rate_with_fallback(c, currency_from, currency_to, date):
    max_retries = 3
    retries = 0

    while retries < max_retries:
        try:
            return c.get_rate(currency_from, currency_to, date)
        except RatesNotAvailableError as e:
            print(f"Exchange rate not available for {currency_from} => {currency_to} on {date}. Retrying... ({retries + 1}/{max_retries})")
            retries += 1
            time.sleep(1)  # Add a delay before retrying

    raise Exception(f"Failed to retrieve exchange rate after multiple attempts: {currency_from} => {currency_to}")

@app.route('/plots', methods=['GET', 'POST'])
def plot():
    # Check if the form is submitted
    if request.method == 'POST':
        # Get the selected currencies from the form
        currency1 = request.form.get('currency1')
        currency2 = request.form.get('currency2')

        end_date = datetime.now()
        start_date = end_date - timedelta(days=90)  # Set the start date as 30 days

        # Generate a date range using pandas
        date_range = pd.date_range(start=start_date, end=end_date, freq='D')  # 'D' means daily frequency

        # Initialize forex_python API
        c = CurrencyRates()

        # Create empty list for exchange rates
        exchange_rates = []

        # Loop through dates and currencies
        for date in date_range:
            date_str = date.strftime("%Y-%m-%d")
            rates_dict = {'date': date_str}
            for currency in [currency1, currency2]:
                try:
                    rate = get_exchange_rate_with_fallback(c, currency1, currency, date)
                    rates_dict[currency] = rate
                except Exception as e:
                    print(f"Error: {e}")
                    # If there is an error, skip this date and move to the next one
                    continue

            exchange_rates.append(rates_dict)

        # Create a pandas DataFrame from the exchange rates
        df = pd.DataFrame(exchange_rates)

        # Round the exchange rates to 4 decimal places
        df = df.round(4)

        # Convert the dates to a datetime format
        df['date'] = pd.to_datetime(df['date'])

        # Plot the exchange rates
        # plt.plot(df['date'], df[currency1], label=currency1)
        plt.plot(df['date'], df[currency2], label=currency2)

        # Add labels and title to the plot
        plt.xlabel('Date')
        plt.ylabel('Exchange Rate')
        plt.title(f'Exchange Rates: {currency1}/{currency2}')

        # Rotate the date labels by 45 degrees
        plt.xticks(rotation=90)

        # Add a legend to the plot
        plt.legend()

        # Save the plot to a file (optional)
        plt.savefig('static/plot.png')  # Save the plot to a file in the 'static' folder

        plt.close()

    # Fetch currency information
    currency_info = get_currency_info()

    # Render the template with the currency information
    return render_template('plots.html', currency_info=currency_info)




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

# This route is designed to render a web page that allows users to select a currency from a dropdown menu and view its exchange rates
@app.route('/exchangeRates')
def exchangeRates():
    currency_info = get_currency_info()
    return render_template('exchangeRates.html', currency_info=currency_info)
