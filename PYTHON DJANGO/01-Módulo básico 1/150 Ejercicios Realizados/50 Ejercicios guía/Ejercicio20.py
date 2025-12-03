# Organizador de lista
santiagoN = [199, 478, 44, 785, 2484, 484, 1, 782, 760, 152]

print("Lista original:", santiagoN)
print("Cantidad de elementos:", len(santiagoN))

# Crear copias para no modificar la original
santiagoAsc = santiagoN.copy() 
santiagoDes = santiagoN.copy()

# Ordenar de menor a mayor
santiagoAsc.sort()
print("\nOrdenada ascendente:", santiagoAsc)

# Ordenar de mayor a menor
santiagoDes.sort(reverse=True)
print("Ordenada descendente:", santiagoDes)

# Mezclar la lista
import random 
santiagoMezcla = santiagoN.copy()
random.shuffle(santiagoMezcla)
print("Lista mezclada:", santiagoMezcla)

# Invertir orden
santiagoInvertido = santiagoN.copy()
santiagoInvertido.reverse()
print("Orden invertido:", santiagoInvertido)
print("\nLista original (sin cambios):", santiagoN)