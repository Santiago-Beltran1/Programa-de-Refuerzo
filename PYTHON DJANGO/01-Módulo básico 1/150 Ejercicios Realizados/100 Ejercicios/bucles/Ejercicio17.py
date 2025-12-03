# Simulación de votaciones

santiagoA = 0
santiagoB = 0

while True:
    santiagoV = input("Vote por A o B (fin para terminar): ").lower()
    if santiagoV == "fin":
        break
    elif santiagoV == "a":
        santiagoA += 1
    elif santiagoV == "b":
        santiagoB += 1
    else:
        print("Voto inválido")

print("Votos A:", santiagoA, "Votos B:", santiagoB)

if santiagoA == santiagoB:
    print("Empate, ninguno gana")
elif santiagoA > santiagoB:
    print("Gana A")
else:
    print("Gana B")
