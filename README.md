# Currency Exchange App
# Exchange Rates

This web application is designed by CSUMB CST205's Team9485 to provide a user-friendly platform for currency exchange.

## Team Members
- Tamanna Zahir
- Rakery Cheng
- Delight Lee
- Haider Syed

## Class Information
- CST205-01_FA23: Multimedia Design & Programming
- Date: 12/11/23

## How to Run the Program
### Prerequisites
- Python (Version 3.x.x recommended)
- Flask (Check compatibility with Python version)
- It's recommended to use a virtual environment for Python projects.

### Set Up Python Environment
1. Make sure Python is installed on your machine.
2. Create a virtual environment:
   ```shell
   python -m venv venv
   
## Activate the virtual environment:
- Windows:  venv\Scripts\activate
- MacOS/Linux: source venv/bin/activate
- 
**Install Required Packages:**
- Install Flask and other required packages using pip.
- This project requires flask, flask_bootstrap, and forex_python.
- Run *pip install Flask Flask-Bootstrap forex-python requests*
- 
## Install Required Packages
- pip install Flask Flask-Bootstrap forex-python requests
**API Key:**
- This project uses an API key for the ExchangeRate-API.
- Ensure you have a valid API key, as the one in your script might be a placeholder.
- EXCHANGE_RATE_API_KEY='2f37f7d40f9163a5c0ba1c85'

**Run the Flask Application:**
- Run the application using flask run. This will start a local web server.
- By default, Flask runs on port 5000. You can access the application by navigating to http://127.0.0.1:5000/

## Link to GitHub repository and Trello board
- GitHub Repo: https://github.com/Tamanna-Zahir/CurrencyExchangeApp.git
- Trello Board: https://trello.com/invite/b/WiNPDqoJ/ATTIbcd39fa634c2121a6a9054a2c0c6d1586B2E27D3/cst205-team-9485-project
## Future work
- The incorporation of historical exchange rates graphing is underway.
  This feature will provide users with visual representations of currency performance over time.
- Plots are talking a while to load as graph spans over 90 days of datapoints. The plotting feature also limited as the API used only have historical data (which can be downloaded as csv files) on certain main currencies. With that said, given more time, another, more efficient API what a more vast datapool would be ideally found and used.
