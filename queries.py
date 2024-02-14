from connessioni import *

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'daitv'
}


def create_db():
    localhost_connect = {
        'host': db_config['host'],
        'user': db_config['user'],
        'password': db_config['password']
    }

    connection = mysql.connector.connect(**localhost_connect)
    cursor = connection.cursor()


    query_drop = f"DROP DATABASE {db_config['database']}"
    cursor.execute(query_drop)
    connection.commit()
    
    
    query_db = f"CREATE DATABASE {db_config['database']}"

    cursor.execute(query_db)
    connection.commit()

    cursor.close()
    connection.close()


def create_tables():
    query= """CREATE TABLE IF NOT EXISTS utente(
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    gender VARCHAR(50),
    age INT,
    work VARCHAR(255),
    cap VARCHAR(5)
    );
    """
    execute_query_insert(query)

    query= """CREATE TABLE IF NOT EXISTS movie(
    movie_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    release_year INT
    );
    """
    execute_query_insert(query)

    query = """CREATE TABLE IF NOT EXISTS rating(
    id_rating INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    movie_id INT,
    valutazione INT,
    timestamp INT,
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES utente(user_id),
    CONSTRAINT fk_movie_user FOREIGN KEY (movie_id) REFERENCES movie(movie_id)
    );
    """
    execute_query_insert(query)

    query = """CREATE TABLE IF NOT EXISTS genres(
    genre_id  INT PRIMARY KEY AUTO_INCREMENT,
    type VARCHAR(255)
    );
    """
    execute_query_insert(query)

    query ="""
    CREATE TABLE IF NOT EXISTS type(
    genre_id INT,
    movie_id INT,
    CONSTRAINT fk_movie_type FOREIGN KEY (movie_id) REFERENCES movie(movie_id),
    CONSTRAINT fk_genre FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
    );
    """
    execute_query_insert(query)


