from connessioni import *
import csv

def inserimento_ratings():
    query = """
    INSERT INTO rating(user_id, movie_id, valutazione, timestamp)
    VALUES (%s,%s,%s,%s)
    """
    with open("Dati/ratings_edit.csv", "r", encoding="utf-8", newline="") as file:
        lettore = csv.reader(file, delimiter=",")
        next(lettore)
        for elem in lettore:
            execute_query_insert(query, (elem[0],elem[1],elem[2],elem[3]))