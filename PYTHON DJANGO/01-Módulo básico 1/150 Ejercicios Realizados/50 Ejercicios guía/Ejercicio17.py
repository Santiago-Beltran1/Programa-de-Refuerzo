# Lista de compras inteligente
santiagoCom = ["arroz", "carne", "lentejas"]

print("Lista inicial: ")
print(santiagoCom)

# Agregar elementos
santiagoCom.append("huevos")
santiagoCom.append("guayabas")

print("\nSe agregan huevos y guayabas, la lista queda: ")
print(santiagoCom)

# Insertar en posición específica
santiagoCom.insert(2, "aceite")
print("\nDespués de insertar el aceite en la posición 2 de la lista: ")
print(santiagoCom)

# Eliminar elementos
santiagoCom.remove("huevos") 
print("\nDespués de eliminar huevos:")
print(santiagoCom)

# Eliminar por posición
santiagoEliminado = santiagoCom.pop(0)
print("\nEliminamos el primer elemento:", santiagoEliminado)
print("Lista final:", santiagoCom)