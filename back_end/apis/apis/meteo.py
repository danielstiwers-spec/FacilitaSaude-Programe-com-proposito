import requests

def tempo():

    url="https://api.open-meteo.com/v1/forecast?latitude=-25.42&longitude=-49.27&current_weather=true"

    return requests.get(url).json()