import pandas as pd
import sqlite3

df=pd.read_excel("dados/TACO.xlsx")

conn=sqlite3.connect("banco/taco.db")

df.to_sql(
    "alimentos",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("TACO importada com sucesso!")