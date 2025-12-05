def SantiagoB(Santiagoseg):
    Santiagoh = Santiagoseg // 3600
    Santiagom = (Santiagoseg % 3600) // 60
    Santiagos = Santiagoseg % 60
    Santiagotiempo = f"{Santiagoh:02}:{Santiagom:02}:{Santiagos:02}"
    print(f"{Santiagoseg} segundos equivalen a {Santiagotiempo}")
    return Santiagotiempo

SantiagoB(17)
SantiagoB(1200)