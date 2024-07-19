#weather API Fetcher
import requests

def fetch_weather(api_key, city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params ={
        'q': city,
        'units':'metric', #use'imperial' for fahrenheit
        'appid': api_key
    }

    #Mkae aget request to the openweatherMap API
    response = requests.get(base_url, params =params)

    if response.status_code ==200:
        #Extract data in JSON format
        weather_data = response.json()

        #extract relavant information
        description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        
        #print the weather information
        print(f"Weather in {city}: {description}")
        print(f"Temperature : {temperature}degree celsius")
        print(f"Humidity: {humidity}%")
    else:
        print(f"Error fetching weather data: {response.status_code}")

        if __name__ == "__main__":
            #prompt the user to eter API key and city name
            api_key = input("Enter your OpenWeatherMap API key:").strip()
            city = input("Enter city name:").strip()

            fetch_weather(api_key,city)

        
