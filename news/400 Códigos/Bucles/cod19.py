def SantiagoBPrimo(SantiagoN):
    if SantiagoN < 2: 
        return False
    for SantiagoI in range(2, int(SantiagoN**0.5) + 1):
        if SantiagoN % SantiagoI == 0:
            return False
        return True
    
for SantiagoN in [2,4,5,8,14,18,20,23]:
    print(f"{SantiagoN} es primo: {SantiagoBPrimo(SantiagoN)}")