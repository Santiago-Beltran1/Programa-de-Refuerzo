SantiagoF = input("Escriba una frase: ")
SantiagoB, SantiagoL, SantiagoNums, SantiagoEsps = 0,0,0,0

while SantiagoB < len(SantiagoF):
    if SantiagoF[SantiagoB].isalpha():
        SantiagoL += 1
    elif SantiagoF[SantiagoB].isdigit():
        SantiagoNums += 1
    elif SantiagoF[SantiagoB].isspace():
        SantiagoEsps += 1
    SantiagoB += 1

print(f"Letras: - {SantiagoL} -  Números: {SantiagoNums} - Espacios:, {SantiagoEsps}")
