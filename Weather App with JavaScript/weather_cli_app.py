import requests
import sys

def get_weather(api_key, location):
    """
    Fetches weather data for a given location using the OpenWeatherMap API.

    Parameters:
        api_key (str): Your OpenWeatherMap API key.
        location (str): The city name or ZIP code.

    Returns:
        dict: Weather data if successful, or None if an error occurs.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit.
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather(data):
    """
    Displays weather information in a user-friendly format.

    Parameters:
        data (dict): Weather data from the OpenWeatherMap API.
    """
    if data:
        location = data.get('name', 'Unknown location')
        main = data.get('main', {})
        weather = data.get('weather', [{}])[0]

        print(f"\nWeather in {location}:")
        print(f"Temperature: {main.get('temp', 'N/A')} °C")
        print(f"Humidity: {main.get('humidity', 'N/A')}%")
        print(f"Condition: {weather.get('description', 'N/A').capitalize()}")
    else:
        print("No weather data available.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python weather_cli_app.py <API_KEY> <LOCATION>")
        sys.exit(1)

    api_key = sys.argv[1]
    location = sys.argv[2]

    weather_data = get_weather(api_key, location)
    display_weather(weather_data)
