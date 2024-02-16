from connessioni import *
import matplotlib.pyplot as plt
from numpy import *
from PIL import Image

connessione = create_db_connection()
cursor = connessione.cursor()

#numero film per ogni anno (hist plot)

#def film_per_anno():
query = """SELECT COUNT(title) AS "Numero film", release_year
FROM movie
GROUP BY release_year;
"""
dati = execute_query(query)
lista_anni_x = []
lista_numeri_y = []
for elem in dati:
    lista_anni_x.append(elem["release_year"])
    lista_numeri_y.append(elem["Numero film"])

diagramma, assi = plt.subplots()
assi.bar(lista_anni_x,lista_numeri_y)
assi.set_xlabel("Anno di rilascio")
assi.set_title("Quanti film ci sono per anno di pubblicazione?")

diagramma.canvas.draw()
buf = diagramma.canvas.tostring_rgb()
width, height = diagramma.canvas.get_width_height()
pil_image = Image.frombytes("RGB", (width, height), buf)
pil_image.save('Dati/film_per_anno.png')

#def film_per_genere():
query = """SELECT COUNT(title) AS "Numero film", genres.type
FROM movie INNER JOIN type INNER JOIN genres
ON movie.movie_id = type.movie_id AND type.genre_id = genres.genre_id
GROUP BY genres.type;
"""
dati = execute_query(query)
lista_anni_x = []
lista_numeri_y = []
for elem in dati:
    lista_anni_x.append(elem["type"])
    lista_numeri_y.append(elem["Numero film"])#nomi liste da cambiare

diagramma2, assi = plt.subplots()
assi.barh(lista_anni_x,lista_numeri_y)
assi.set_xlabel("Numero di film")
assi.set_title("Quanti film ci sono per ogni genere?")

diagramma2.canvas.draw()
buf = diagramma2.canvas.tostring_rgb()
width, height = diagramma2.canvas.get_width_height()
pil_image = Image.frombytes("RGB", (width, height), buf)
pil_image.save('Dati/film_per_genere.png')