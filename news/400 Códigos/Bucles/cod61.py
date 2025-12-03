SantiagoBCant = int(input("Cuántos números desea ingresar: "))
SantiagoPos = 0
SantiagoNeg = 0
Santiago0 = 0

for SantiagoI in range(SantiagoBCant):
    SantiagoNum = float(input("Ingrese un número: "))
    if SantiagoNum > 0:
        SantiagoPos += 1
    elif SantiagoNum < 0:
        SantiagoNeg += 1
    else:
        Santiago0 += 1

print("Positivos:", SantiagoPos)
print("Negativos:", SantiagoNeg)
print("Ceros:", Santiago0)
