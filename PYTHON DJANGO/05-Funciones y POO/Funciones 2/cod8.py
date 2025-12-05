def SantiagoP(SantiagoN):
    if SantiagoN < 2:
        return False
    for SantiagoDiv in range(2, int(SantiagoN**0.5)+1):
        if SantiagoN % SantiagoDiv == 0:
            return False
    return True

def SantiagoGen(SantiagoLimit):
    return [SantiagoNum for SantiagoNum in range(2, SantiagoLimit+1) if SantiagoP(SantiagoNum)]

print(f"Lista de números primos hasta el número 45: {SantiagoGen(45)}")
