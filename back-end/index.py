
import requests

url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"

dados = requests.get(url).json()

for estado in dados:
    print(estado["nome"])

import requests

codigo = "7891000100103"

url = f"https://world.openfoodfacts.org/api/v0/product/{codigo}.json"

produto = requests.get(url).json()

print(produto["product"]["product_name"])

import pandas as pd

df = pd.read_excel("TACO.xlsx")

print(df.head())
print(df.columns)

import sqlite3
import pandas as pd

conn = sqlite3.connect("taco.db")

df = pd.read_excel("TACO.xlsx")

df.to_sql(
    "alimentos",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

import requests

url = "https://wger.de/api/v2/exercise/"

dados = requests.get(url).json()

print(dados)

import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=-25.42&longitude=-49.27&current_weather=true"

dados = requests.get(url).json()

print(dados)

import wikipedia

wikipedia.set_lang("pt")

print(wikipedia.summary("Capivara", sentences=3))

from qwikidata.linked_data_interface import get_entity_dict_from_api

entity = get_entity_dict_from_api("Q7378")

print(entity)