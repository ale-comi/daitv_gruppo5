import json
import mysql.connector
from flask import Flask, jsonify, render_template, request, redirect, url_for
from connessioni import *

app = Flask(__name__)

@app.route("/")
def homepage():

    query = "SELECT title, release_year FROM movie"
    movie = execute_query(query)
    print(movie)

    return render_template("test2Bootstrap.html", movie=movie)

if __name__ == '__main__':
    app.run(debug=True)