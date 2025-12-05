class SantiagoPrio:
    def __init__(self, SantiagoNom, SantiagoPrio):
        self.SantiagoNom = SantiagoNom
        self.SantiagoPrio = SantiagoPrio


def SantiagoOrd(SantiagoList):
    return sorted(SantiagoList, key=lambda SantiagoT: SantiagoT.SantiagoPrio)


SantiagoT = [SantiagoPrio("Dormir", 2), SantiagoPrio("Estudio", 1)]
SantiagoOrdenadas = SantiagoOrd(SantiagoT)
print([t.SantiagoNom for t in SantiagoOrdenadas])
