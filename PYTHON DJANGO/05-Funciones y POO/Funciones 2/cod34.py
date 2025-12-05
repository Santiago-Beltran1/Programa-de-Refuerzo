def SantiagoOT(SantiagoLT):
    return sorted(SantiagoLT, key=lambda SantiagoT: SantiagoT[1])

SantiagoT = [("SantiagoA", 55), ("SantiagoB", 22), ("SantiagoC", 90)]
print(SantiagoOT(SantiagoT))
