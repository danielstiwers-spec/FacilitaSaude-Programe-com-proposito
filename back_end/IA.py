from apis.ibge import listar_estados
from apis.wikipedia import pesquisar
from apis.meteo import clima
from apis.openfoodfacts import produto

from apis.ibge import listar_estados

dados=listar_estados()

for estado in dados:
    print(estado["nome"])

    from apis.wikipedia import pesquisar

print(pesquisar("Capivara"))

import sqlite3

conn=sqlite3.connect("banco/taco.db")

cursor=conn.cursor()

cursor.execute("""

SELECT *
FROM alimentos
WHERE Alimento LIKE '%banana%'

""")

print(cursor.fetchall())