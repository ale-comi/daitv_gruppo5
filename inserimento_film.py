from connessioni import *
import csv

def inserimento_film():
    query_insert = """
    INSERT INTO movie(title, release_year) 
    VALUES (%s, %s)
    """

    file = open("Dati/elenco_corretto.csv", mode="r", encoding="utf-8", newline="")

    lettore = csv.reader(file, delimiter=",")

    next(lettore)

    for riga in lettore:

        execute_query_insert(
            query_insert,
            (
                riga[1],
                riga[2],

            ))
