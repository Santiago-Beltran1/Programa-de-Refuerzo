# Juego de adivinanza
santiagoAdi = 12
SantiagoEncontrar = int(input("Adivine el número, ingrese su número: "))

print("Tu adivinanza es:", SantiagoEncontrar)

if SantiagoEncontrar == santiagoAdi: 
    print("¡FELICIDADES! Adivinaste el número, el número secreto era: ", santiagoAdi)
elif SantiagoEncontrar < santiagoAdi:
    print("Tu número es menor. Intenta con uno más grande")
else:
    print("Tu número es mayor. Intenta con uno más pequeño")