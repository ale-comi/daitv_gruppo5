import json
import mysql.connector
from flask import Flask, jsonify, render_template, request, redirect, url_for
from connessioni import *

app = Flask(__name__)

@app.route("/<int:pagina>")
def homepage_data(pagina):

    query = f"""
        SELECT title, release_year 
        FROM movie
        LIMIT 48
        OFFSET {(pagina - 1) * 48};
        """
    
    movie = execute_query(query)
    return jsonify({'movie': movie})


@app.route("/generi")
def generi_data():
    query = f"""
        SELECT type 
        FROM genres;
        """

    genres = execute_query(query)
    return jsonify({'genres': genres})

@app.route("/")
def homepage(pagina=1):
    home_data = homepage_data(pagina)
    data = json.loads(home_data.get_data(as_text=True))
    movies = data['movie']

    genres_data = generi_data()
    data1 = json.loads(genres_data.get_data(as_text=True))
    genres = data1['genres']

    return render_template("test2Bootstrap.html", movies=movies, genres=genres)


# Nuovo percorso per gestire le richieste AJAX e restituire i dati dei film
@app.route('/get_movies', methods=['GET'])
def get_movies():
    genere_selezionato = request.args.get('genere')

    # Esegui una query al database con il genere selezionato e recupera i dati dei film pertinenti
    # Sostituisci questo con la tua logica di query al database effettiva
    # Esempio: dati_film = query_database(genere_selezionato)
    query = f"""
            SELECT title, release_year 
            FROM movie AS m JOIN type AS t 
            ON m.movie_id=t.movie_id 
            JOIN genres AS g 
            ON g.genre_id=t.genre_id 
            WHERE g.type = '{genere_selezionato}'
            """
    dati_film = execute_query(query)

    # Rendi un template o crea una risposta JSON con i dati dei film
    return render_template('filtriGeneri.html', dati_film=dati_film)

if __name__ == '__main__':
    app.run(debug=True)