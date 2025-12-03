def SantiagoPalin(SantiagoT):
    SantiagoT = SantiagoT.replace(" ", "").lower()
    return SantiagoT == SantiagoT[::-1]

print(f"La palabra SOMOS es palíndroma: {SantiagoPalin("SOMOS")}")
