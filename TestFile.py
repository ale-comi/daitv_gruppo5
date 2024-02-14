import csv

with open("Elenco Movies definitivo.csv", "r", encoding="utf-8") as file:
    lettore = csv.reader(file)
    next(file)
    generi = set()
    indici = []
    with open("Elenco_corretto.csv", "w", encoding="utf-8", newline="") as file_nuovo:
        scrittore = csv.writer(file_nuovo)
        c = 1
        file_nuovo.write("MovieID,Title,Year,Genres"+"\n")
        for elem in lettore:
            if elem[0] == "16":
                elem[1] = "Casino (1995)"
            if elem[0] == "3936":
                elem[1] = "Phantom of the opera, The (1943)"
            if elem[0] == "3785":
                elem[2] = "Comedy|Horror"
            if elem[2] == "Dramma":
                elem[2] = "Drama"

            titolo_separato = elem[1][:elem[1].rfind("(")].strip()
            anno_separato = elem[1].split("(")[-1].strip(" )")
            genere_separato = elem[2].split("|")
            if "," in titolo_separato:
                stringa = f'{str(c)},"{titolo_separato}",{anno_separato}'
            else:
                stringa = f"{str(c)},{titolo_separato},{anno_separato}"
            finale =""
            for i, genere in enumerate(genere_separato):
                if i == 0:
                    finale+= f"{genere}"
                else:
                    finale+= f",{genere}"
            stringa += f',"{finale}"'
            c+=1
            file_nuovo.write(stringa+"\n")



