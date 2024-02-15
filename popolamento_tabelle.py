from connessioni import *
# import mysql.connector
import csv

connessione = create_db_connection()
cursor = connessione.cursor()

def elenco_generi():
    set_generi = set()

    with open("Dati/elenco_corretto.csv", mode="r", encoding="utf-8", newline="") as file:

        lettore = csv.reader(file, delimiter=",")

        next(lettore)

        for riga in lettore:
            riga = riga[3].strip("\"").split(",")
            for i in riga:
                set_generi.add(i)

    
    lista_generi = list(set_generi)

    return lista_generi



def inserimento_film():
    query_insert = """
    INSERT INTO movie(movie_id, title, release_year) 
    VALUES (%s, %s, %s)
    """

    with open("Dati/elenco_corretto.csv", mode="r", encoding="utf-8", newline="") as file:

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
    lista_generi = elenco_generi()

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

    for _ in range(size // dim + 1):

        params = [
            (elem[0],elem[1],elem[2],elem[3])
            for elem in lista_rating[i : j :]
            ]
        
        cursor.executemany(query, params)
        connessione.commit()

        print(j)

        i += dim
        j += dim

        #ad ultimo ciclo assegno a j il valore dell'ultimo elemento +1
        if j >= size:
            j = j + (size % dim) - dim + 1


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


def inserimento_type():
    with (open("Dati/elenco_corretto.csv", mode="r", encoding="utf-8", newline="") as file2):
        lettore = csv.reader(file2)
        next(lettore)
        lista_film_generi = []
        for elem in lettore:
            lista_film_generi.append({"id_film":elem[0], "generi":elem[3].split(",")})

    lista_generi = elenco_generi()

    
    diz_genere = {}

    query_genere = """SELECT genre_id, type
    FROM genres
    """

    lista_diz_colonne = execute_query(query_genere)

    for diz in lista_diz_colonne:
        diz_genere[diz["type"]] = diz["genre_id"]


    print(lista_film_generi)
    print( diz_genere)

    #1) creo dizionario nome: id
    #faccio for per lista_film_generi, sostituisco il nome genere all'id nella lista
    #eventuale sleep per evitare conflitto 
    #carico in batch questa lista come sopra


    
    # for elem in lista_film_generi:


    # for elem in lista_film_generi:
    #     id_generi = []
    #     for genere in elem["generi"]:
    #         id_corrispondente = execute_query(query_id_genere, (genere,))
    #         id_generi.append(id_corrispondente[0]["genre_id"])
    #     elem["generi"] = id_generi

    # query = """
    #     INSERT INTO type(genre_id, movie_id)
    #     VALUES (%s,%s)
    #     """
    # print("Query inserimento in corso...")
    # for elem in lista_film_generi:
    #     for genere in elem["generi"]:
    #         execute_query_insert(query, (genere, elem["id_film"]))
    # print("Dati caricati")