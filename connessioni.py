import mysql.connector
from mysql.connector import Error

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'daitv'
}


def create_db(drop=True):
    localhost_connect = {
        'host': db_config['host'],
        'user': db_config['user'],
        'password': db_config['password']
    }

    connection = mysql.connector.connect(**localhost_connect)
    cursor = connection.cursor()

    if drop:
        query_drop = f"DROP DATABASE {db_config['database']};"
        cursor.execute(query_drop)
        connection.commit()
    
    
    query_db = f"CREATE DATABASE {db_config['database']};"

    cursor.execute(query_db)
    connection.commit()

    cursor.close()
    connection.close()

def create_db_connection():
    return mysql.connector.connect(**db_config)

def execute_query(query, params=None):
    connection = create_db_connection()
    cursor = connection.cursor(dictionary=True)
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def execute_query_insert(query, params=None):
    connection = create_db_connection()
    cursor = connection.cursor()

    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)

    connection.commit()

    cursor.close()
    connection.close()


def execute_many(query, data):
    connection = create_db_connection()
    cursor = connection.cursor()
    try:
        cursor.executemany(query, data)
        connection.commit()
        print("Query succesful")
    except Error as err:
        print(f"Error: '{err}'")