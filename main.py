import connessioni as conn
import queries as queries
import popolamento_tabelle as pt
import time

try:
    conn.create_db(drop=False)
    queries.create_tables()
except:
    pass

# pt.inserimento_film()
# pt.inserimento_utente()
# pt.inserimento_generi()
# pt.inserimento_ratings()
pt.inserimento_type()
 #type


