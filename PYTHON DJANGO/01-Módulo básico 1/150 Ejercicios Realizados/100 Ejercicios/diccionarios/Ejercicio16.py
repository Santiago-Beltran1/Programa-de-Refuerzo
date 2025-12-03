#Identificador de el producto más caro que se encuentre

santiagoProds = {"Portátil": 3000000, "SSD": 250000, "Celular": 1500000}
santiagoMasCaro = max(santiagoProds, key=santiagoProds.get)

print(f"El producto más caro es {santiagoMasCaro} con precio {santiagoProds[santiagoMasCaro]}")
