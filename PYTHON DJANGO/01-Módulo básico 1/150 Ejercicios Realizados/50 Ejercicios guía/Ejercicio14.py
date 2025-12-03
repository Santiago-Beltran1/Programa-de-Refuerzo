# Detector de números pares
santiagoN = 1 
santiagoLimi = 20 
santiagoPar = 0 

print("Los números pares entre el 1 y el", santiagoLimi, "son : ")

while santiagoN <= santiagoLimi:
    if santiagoN % 2 == 0: # % es el operador módulo (resto de división)
        print(santiagoN, "es par")
        santiagoPar = santiagoPar + 1
    santiagoN = santiagoN + 1

print("\nResumen:")
print("Se encontraron", santiagoPar, "números pares")
