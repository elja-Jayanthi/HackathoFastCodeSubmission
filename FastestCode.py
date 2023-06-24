import requests
import json

# create a function to read the weather forecast from an API
def get_weather_forecast(City):
    """This function returns the weather forecast for the given city, Please change the API key to your own key"""
    api_Key='b1198698e034294487785698a5510f7a'
    city=City
    api_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city +"&units=metric&appid=b1198698e034294487785698a5510f7a"
    r = requests.get(api_url)
    if (r.status_code==200):
        return r.json()
    else:
        print("Invalid City Name")
        exit()
    

# create a function to parse the JSON response and print the forecast
def parse_weather_forecast(forecast):
    print(forecast['name'])
    print(forecast['weather'][0]['main'])
    print(forecast['weather'][0]['description'])
    print(str(forecast['main']['temp']))


# main function
def main(): 
    City=input("Enter the city name with country code:")
    forecast = get_weather_forecast(City)
    parse_weather_forecast(forecast)


# verify the given city is valid or not
def verify_city(City):
    api_Key='b1198698e034294487785698a5510f7a'
    city=City
    api_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city +"&units=metric&appid=b1198698e034294487785698a5510f7a"
    r = requests.get(api_url)
    if r.status_code==200:
        return True
    else:
        return False

# run the main function
if __name__ == "__main__":
    main()

# Path: FastestCode.py



