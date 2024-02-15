import connessioni as conn
import queries as queries
import popolamento_tabelle as pt
import time

try:
    conn.create_db()
    queries.create_tables()
except:
    pass

pt.inserimento_film()
pt.inserimento_utente()
pt.inserimento_generi()
pt.inserimento_ratings()
print("Wait 10 second")
time.sleep(50)
print("inizio metodo type")
pt.inserimento_type()
 #type


