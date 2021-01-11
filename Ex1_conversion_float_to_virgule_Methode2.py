saisi_str = input("Sasir un flottant: ")
saisi_float = float(saisi_str)
print("Le nombre flottant saisi est: ",saisi_float)

maListe = saisi_str.split(".")
print("le type de maListe est : ",type(maListe))
print("Ma liste est :",maListe)


monFlottant = ",".join(maListe)
print("Mon nombre avec virgule est ", monFlottant)
