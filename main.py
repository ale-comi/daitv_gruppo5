import connessioni as cn
import queries as qs
import inserimento_film as inf
import inserimento_generi as ig
import inserimento_ratings  as ir
import inserimento_user as iu

try:



    qs.create_db()
    qs.create_tables()

    inf.inserimento_film()
    ig.inserimento_generi()
    iu.inserimento_utente()
    ir.inserimento_ratings()


except:
    pass

