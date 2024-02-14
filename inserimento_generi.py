from connessioni import *
import csv

def inserimento_generi():
    set_generi = set()

    file = open("Dati/elenco_corretto.csv", mode="r", encoding="utf-8", newline="")

    lettore = csv.reader(file, delimiter=",")

    next(lettore)

    set_generi = set()

    for riga in lettore:
        riga = riga[3].strip("\"").split(",")
        for i in riga:
            set_generi.add(i)

    lista_generi = list(set_generi)

    query_insert = """
    INSERT INTO genres(type) 
    VALUES (%s)
    """

    for i in lista_generi:
        execute_query_insert(
            query_insert,
            (
                i,
            ))


