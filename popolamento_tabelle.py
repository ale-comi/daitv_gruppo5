from connessioni import *
# import mysql.connector
import csv

connessione = create_db_connection()
cursor = connessione.cursor()


def inserimento_film():
    query_insert = """
    INSERT INTO movie(movie_id, title, release_year) 
    VALUES (%s, %s, %s)
    """

    file = open("Dati/elenco_corretto.csv", mode="r", encoding="utf-8", newline="")

    lettore = csv.reader(file, delimiter=",")

    next(lettore)

    for riga in lettore:

        execute_query_insert(
            query_insert,
            (
                riga[0],
                riga[1],
                riga[2]

            ))
        

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
        

def inserimento_ratings():
    query = """
    INSERT INTO rating(user_id, movie_id, valutazione, timestamp)
    VALUES (%s,%s,%s,%s)
    """

    lista_rating = []

    with open("Dati/ratings_edit.csv", "r", encoding="utf-8", newline="") as file:
        lettore = csv.reader(file, delimiter=",")
        next(lettore)
        for elem in lettore:
            lista_rating.append(elem)
    

    dim = 10000
    i = 0
    j = 10000
    size = len(lista_rating)
    print(size)
    print(lista_rating[1000208])

    while size >= j:
   
        params = [
            (elem[0],elem[1],elem[2],elem[3])
            for elem in lista_rating[i : j :]
            ]

        cursor.executemany(query, params)
        connessione.commit()

        i += dim
        j += dim

        print(j)
  

def inserimento_utente():
    query = """
    INSERT INTO utente(gender, age, work, cap)
    VALUES (%s, %s, %s, %s)
    """

    with open("Dati/users_edit.csv", "r", encoding="utf-8", newline="") as file:
        lettore = csv.reader(file, delimiter=",")
        next(lettore)
        for elem in lettore:
            execute_query_insert(query, (elem[1], elem[2], elem[4], elem[3]))



    


