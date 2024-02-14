import connessioni as conn
import queries as queries
import popolamento_tabelle as pt

try:
    conn.create_db()
    queries.create_tables()
except:
    pass

pt.inserimento_film()
pt.inserimento_utente()
pt.inserimento_generi()
pt.inserimento_ratings()
#pt.inserimento_type()
 #type


