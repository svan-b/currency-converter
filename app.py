from flask import Flask, render_template
import os
from currencyconverter import converter  # Import the module from your package

app = Flask(__name__)

@app.route('/')
def index():
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
    from_currency = 'USD'
    to_currency = 'EUR'
    historical_data = converter.get_historical_exchange_rate(api_key, from_currency, to_currency)
    return render_template('index.html', historical_data=historical_data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
