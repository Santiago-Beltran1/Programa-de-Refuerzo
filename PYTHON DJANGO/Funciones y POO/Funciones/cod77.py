def SantiagoBCesar(SantiagoBTexto, SantiagoBDesplazamiento):
    SantiagoBResultado = ""
    for c in SantiagoBTexto:
        if c.isalpha():
            SantiagoBase = ord('A') if c.isupper() else ord('a')
            SantiagoBResultado += chr((ord(c) - SantiagoBase + SantiagoBDesplazamiento) % 26 + SantiagoBase)
        else:
            SantiagoBResultado += c
    return SantiagoBResultado

SantiagoT = input("Texto a codificar: ")
SantiagoDesp = int(input("Desplazamiento: "))
SantiagoCodi = SantiagoBCesar(SantiagoT, SantiagoDesp)
print("Texto codificado:", SantiagoCodi)
print("Texto decodificado:", SantiagoBCesar(SantiagoCodi, -SantiagoDesp))
