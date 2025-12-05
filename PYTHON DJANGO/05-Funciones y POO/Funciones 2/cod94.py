def SantiagoValT(SantiagoNum):
    SantiagoSum = 0
    SantiagoRever = SantiagoNum[::-1]
    for SantiagoI, SantiagoDig in enumerate(SantiagoRever):
        SantiagoD = int(SantiagoDig)
        if SantiagoI % 2 == 1:
            SantiagoD *= 2
            if SantiagoD > 9:
                SantiagoD -= 9
        SantiagoSum += SantiagoD
    if SantiagoSum % 10 == 0:
        print(f"Tarjeta válida: {SantiagoNum}")
    else:
        print(f"Tarjeta inválida: {SantiagoNum}")

SantiagoValT("010445484045")
SantiagoValT("00150405444888")
