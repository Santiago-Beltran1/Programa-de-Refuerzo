# El usuario ingresa 3 nombres

santiagoNoms = tuple(input(f"Ingrese el nombre {i+1}: ") for i in range(3))

print("Nombres guardados en la tupla:", santiagoNoms)
