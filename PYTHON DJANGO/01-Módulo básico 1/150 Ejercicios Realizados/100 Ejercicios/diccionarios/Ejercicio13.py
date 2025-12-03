#Imprime el valor más largo que hay en un diccionario

santiagoDic = {"perro": 1, "elefante": 2, "gato": 3}
santiagoPass = max(santiagoDic.keys(), key=len)
print("La palabra más larga es:", santiagoPass)
