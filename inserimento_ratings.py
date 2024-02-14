from connessioni import *
import csv

with open("Dati/ratings_edit.csv", "r", encoding="utf-8", newline="") as file:
    lettore = csv.reader(file, delimiter=",")
    next(lettore)
    for elem in lettore:
        print(elem)