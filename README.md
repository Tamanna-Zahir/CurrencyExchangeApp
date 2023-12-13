# Exchange Rates
## This project is created by CSUMB CST205's Team9485
- Project Description: This web application is designed to provide users a user-friendly platform for currency exchange.
- Team members: Tamanna Zahir, Rakery Cheng, Delight Lee, and Haider Syed
- Class: CST205-01_FA23: Multimedia Design & Progmng
- Date: 12/11/23
  
## How to run program: 
**Set Up Python Environment:**
- Make sure you have Python installed on your machine(Check Flask compatability)
- It's recommended to use a virtual environment for Python projects. 
- You can create one using python -m venv venv and activate it with source venv\Scripts\activate.ps1(Windows)

**Install Required Packages:**
- Install Flask and other required packages using pip.
- This project requires flask, flask_bootstrap, and forex_python.
- Run *pip install Flask Flask-Bootstrap forex-python requests*

**API Key:**
- This project uses an API key for the ExchangeRate-API.
- Ensure you have a valid API key, as the one in your script might be a placeholder. 

**Run the Flask Application:**
- Run the application using flask run. This will start a local web server.
- By default, Flask runs on port 5000. You can access the application by navigating to http://127.0.0.1:5000/

## Link to GitHub repository and Trello board
- GitHub Repo: https://github.com/delightgit/CST205-Team-9485-Project#cst205-team-9485-project
- Trello Board: https://trello.com/invite/b/WiNPDqoJ/ATTIbcd39fa634c2121a6a9054a2c0c6d1586B2E27D3/cst205-team-9485-project
## Future work
- Current sorting functionality does not accommodate exchange rates that fall below 0.
  Plans are in place to address this limitation and ensure that all exchange rates can be sorted accurately.
- The incorporation of historical exchange rates graphing is underway.
  This feature will provide users with visual representations of currency performance over time.
