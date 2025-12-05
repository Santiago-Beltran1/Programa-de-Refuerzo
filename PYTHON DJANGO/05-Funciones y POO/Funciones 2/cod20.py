import itertools as SantiagoIter

def SantiagoComb(SantiagoList, SantiagoR):
    return list(SantiagoIter.combinations(SantiagoList, SantiagoR))

SantiagoElemens = ["SantiagoA", "SantiagoB", "SantiagoC"]
print(SantiagoComb(SantiagoElemens, 2))
