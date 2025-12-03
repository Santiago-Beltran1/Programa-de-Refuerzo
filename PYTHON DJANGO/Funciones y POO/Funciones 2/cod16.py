def SantiagoPar(SantiagoList):
    return list(filter(lambda SantiagoNum: SantiagoNum % 2 == 0, SantiagoList))

def SantiagoImp(SantiagoLista):
    return list(filter(lambda SantiagoNum: SantiagoNum % 2 != 0, SantiagoLista))

SantiagoNums = [1,2,3,4,5,6]
print(f"Números pares de la lista en otra lista: {SantiagoPar(SantiagoNums)}")
print(f"Números impares de la lista en otra lista: {SantiagoImp(SantiagoNums)}")
