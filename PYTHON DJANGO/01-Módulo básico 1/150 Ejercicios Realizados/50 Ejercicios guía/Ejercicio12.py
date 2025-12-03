# Tabla de multiplicar
santiagoN = int(input("Ingrese un número para ver su tabla de multiplicar hasta el 10: "))

santiagoMul = 1 

print("Tabla de multiplicar del", santiagoN, ": ")
print("=" * 25) 

while santiagoMul <= 10:
    r = santiagoN * santiagoMul
    print(santiagoN, "x", santiagoMul, "=", r)
    santiagoMul = santiagoMul + 1

print("=" * 25)
print("¡Tabla completa!")