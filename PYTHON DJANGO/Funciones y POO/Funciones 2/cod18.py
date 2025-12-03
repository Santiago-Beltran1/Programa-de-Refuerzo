def SantiagoFib(SantiagoLim):
    SantiagoSerie = [0, 1]
    while SantiagoSerie[-1] + SantiagoSerie[-2] < SantiagoLim:
        SantiagoSerie.append(SantiagoSerie[-1] + SantiagoSerie[-2])
    return SantiagoSerie

print(SantiagoFib(200))
