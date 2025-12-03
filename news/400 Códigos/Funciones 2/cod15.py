import numpy as SantiagoNp

def SantiagoGenM(SantiagoFilas, SantiagoCol):
    return SantiagoNp.random.randint(0, 10, (SantiagoFilas, SantiagoCol))

print(SantiagoGenM(2, 2))
