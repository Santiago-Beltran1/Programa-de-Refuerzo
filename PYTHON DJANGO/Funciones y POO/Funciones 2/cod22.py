def SantiagoFacto(SantiagoNum):
    if SantiagoNum == 0 or SantiagoNum == 1:
        return 1
    return SantiagoNum * SantiagoFacto(SantiagoNum-1)

print(f"Factorial de 8: {SantiagoFacto(8)}")
