SantiagobSald = 1460000
SantiagoTra = [("depósito", 800000), ("retiro", 175000), ("retiro", 200000)]

for SantiagoTipo, SantiagoValor in SantiagoTra:
    if SantiagoTipo == "depósito":
        SantiagobSald += SantiagoValor
    else:
        SantiagobSald -= SantiagoValor
print("Saldo final:", SantiagobSald)
