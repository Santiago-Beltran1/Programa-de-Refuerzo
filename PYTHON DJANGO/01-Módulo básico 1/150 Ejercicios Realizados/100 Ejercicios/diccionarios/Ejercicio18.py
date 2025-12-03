#Identificador de todos los elementos que hay sin contar repetidos

santiagoCols = {"c1": "rojo", "c2": "azul", "c3": "rojo"}
santiagoUnics = len(set(santiagoCols.values()))

print("Cantidad de colores únicos:", santiagoUnics)
