from connessioni import *
import csv

set_generi = set()

file = open("Dati/elenco_corretto.csv", mode="r", encoding="utf-8", newline="")

lettore = csv.reader(file, delimiter=",")

next(lettore)

for riga in lettore:
    set_generi.add(riga[3])

query_insert = """
INSERT INTO genres(type) 
VALUES (%s)
"""

for i in set_generi:
    execute_query_insert(
        query_insert,
        (
            riga[3],
        ))
