SantiagoB = "Santiago2025Beltran2026"
SantiagoL = SantiagoN = 0
for SantiagoC in SantiagoB:
    if SantiagoC.isalpha():
        SantiagoL += 1
    elif SantiagoC.isdigit():
        SantiagoN += 1
print("Letras en la frase:", SantiagoL, "Números en la frase:", SantiagoN)
