import connessioni as conn
import queries as queries
import popolamento_tabelle as pt

# drop=True --> viene cancellato e ricreato per intero il database, errore se db non esiste
# drop=False --> il database non viene modificato, lo crea nuovo se non esiste

try:
    conn.create_db(drop=True)
    queries.create_tables()
except:
    pass

pt.inserimento_film()
pt.inserimento_utente()
pt.inserimento_generi()
pt.inserimento_ratings()
pt.inserimento_type()


