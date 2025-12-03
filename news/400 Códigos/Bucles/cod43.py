SantiagoB = [-77, 7, 24, 10, 0, 0, 747, -1]
SantiagoPos = SantiagoNeg = Santiago0 = 0
for SantiagoB in SantiagoB:
    if SantiagoB > 0:
        SantiagoPos += 1
    elif SantiagoB < 0:
        SantiagoNeg += 1
    else:
        Santiago0 += 1
print("Positivos:", SantiagoPos, "Negativos:", SantiagoNeg, "Ceros:", Santiago0)
