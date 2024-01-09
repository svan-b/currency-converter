import os
import requests

def get_historical_exchange_rate(api_key, from_currency, to_currency):
    """
    Fetch historical exchange rates using the Alpha Vantage API.

    :param api_key: Your API key for Alpha Vantage.
    :param from_currency: The currency code to convert from.
    :param to_currency: The currency code to convert to.
    :return: Historical exchange rates.
    """
    url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'FX_DAILY',  # For daily data; you can adjust as needed
        'from_symbol': from_currency,
        'to_symbol': to_currency,
        'apikey': api_key,
        'outputsize': 'compact'  # or 'full' for more data
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        print("Fetched Data:", data)
        # Extracting only the 'Time Series FX (Daily)' part of the response
        time_series = data['Time Series FX (Daily)']
        return time_series
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'An error occurred: {err}')
    return None


if __name__ == '__main__':
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
    if not api_key:
        raise ValueError("API key not found. Set the ALPHA_VANTAGE_API_KEY environment variable.")

    from_currency = 'USD'
    to_currency = 'EUR'

    # Test historical data function
    historical_data = get_historical_exchange_rate(api_key, from_currency, to_currency)
    print("Historical Data:")
    for date, rate_info in list(historical_data.items())[:5]:  # Print first 5 days of data
        print(f"{date}: {rate_info['4. close']}")

