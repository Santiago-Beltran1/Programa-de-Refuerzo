SantiagoDec = int(input("Ingrese un número decimal: "))
SantiagoBin = ""

while SantiagoDec > 0:
    SantiagoBin = str(SantiagoDec % 2) + SantiagoBin
    SantiagoDec //= 2

print(f"El número decimal pasado a binario es: {SantiagoBin}")
