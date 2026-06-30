import requests

def listar():

    url="https://wger.de/api/v2/exercise/"

    return requests.get(url).json()