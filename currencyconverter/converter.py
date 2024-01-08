import os
import requests

def get_exchange_rate(from_currency, to_currency):
    """
    Fetch the real-time exchange rate using Alpha Vantage API.

    :param from_currency: The currency code to convert from.
    :param to_currency: The currency code to convert to.
    :return: The exchange rate.
    """
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
    if not api_key:
        raise ValueError("API key not found. Set the ALPHA_VANTAGE_API_KEY environment variable.")
    
    url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'CURRENCY_EXCHANGE_RATE',
        'from_currency': from_currency,
        'to_currency': to_currency,
        'apikey': api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        data = response.json()
        exchange_rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
        return float(exchange_rate)
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6+
    except Exception as err:
        print(f'An error occurred: {err}')
    return None

if __name__ == '__main__':
    from_currency = 'USD'
    to_currency = 'EUR'  # You can change 'EUR' to any other currency code you want to check against USD

    rate = get_exchange_rate(from_currency, to_currency)
    if rate is not None:
        print(f"The exchange rate from {from_currency} to {to_currency} is: {rate}")
    else:
        print("Failed to retrieve the exchange rate.")
