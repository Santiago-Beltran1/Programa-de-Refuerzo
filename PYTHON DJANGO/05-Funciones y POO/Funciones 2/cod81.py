def SantiagoConve(SantiagoValor, SantiagoUOrigen, SantiagoUDest):
    SantiagoFacto = {"m":1, "cm":100, "mm":1000, "km":0.001}
    SantiagoR = SantiagoValor * SantiagoFacto[SantiagoUDest] / SantiagoFacto[SantiagoUOrigen]
    print(f"{SantiagoValor} {SantiagoUOrigen} equivalen a {SantiagoR} {SantiagoUDest}")

SantiagoConve(15000, "m", "km")
SantiagoConve(7, "km", "m")
