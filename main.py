# drop=True --> viene cancellato e ricreato per intero il database, errore se db non esiste
# drop=False --> il database non viene modificato, lo crea nuovo se non esiste

import connessioni as conn
import queries as queries

try:
    conn.create_db(drop=False)
    queries.create_tables()

    import popolamento_tabelle as pt

    pt.inserimento_film()
    pt.inserimento_utente()
    pt.inserimento_generi()
    pt.inserimento_ratings()
    pt.inserimento_type()
except:
    print("\nOperazioni fermate, è già presente un database! \nPer eliminarlo e caricarlo nuovamente utilizzare il parametro 'drop=True'\n")

