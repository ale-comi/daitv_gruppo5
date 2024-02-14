from connessioni import *
import csv

query = """
INSERT INTO utente(gender, age, work, cap)
VALUES (%s, %s, %s, %s)
"""

with open("Dati/users_edit.csv", "r", encoding="utf-8", newline="") as file:
    lettore = csv.reader(file, delimiter=",")
    next(lettore)
    for elem in lettore:
        execute_query_insert(query, (elem[1], elem[2], elem[4], elem[3]))