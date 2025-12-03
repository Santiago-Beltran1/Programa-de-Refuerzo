def SantiagoBDecimalABinario(SantiagoDecimal):
    return bin(SantiagoDecimal)[2:]

SantiagoN = int(input("Ingresa un número decimal: "))
print(f"Binario: {SantiagoBDecimalABinario(SantiagoN)}")

