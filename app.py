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
        LIMIT 100
        OFFSET {(pagina - 1) * 100};
        """
    
    movie = execute_query(query)
    return jsonify({'movie': movie})

@app.route("/")
def homepage(pagina=1):
    home_data = homepage_data(pagina)
    data = json.loads(home_data.get_data(as_text=True))
    movies = data['movie']

    return render_template("test2Bootstrap.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)