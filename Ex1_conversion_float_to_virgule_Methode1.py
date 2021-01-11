saisi_str = input("Sasir un flottant: ")
saisi_float = float(saisi_str)
print("Le nombre flottant saisi est: ",saisi_float)

entiere, decimale = saisi_str.split(".")

monNombe =",".join([entiere,decimale])
print("mon nombre est ",monNombe)
