# Archivo cod17.py
import time as SantiagoTime

def SantiagoMed(SantiagoFnc):
    def SantiagoWrapper(*SantiagoArgs, **SantiagoKwargs):
        SantiagoIni = SantiagoTime.time()
        SantiagoR = SantiagoFnc(*SantiagoArgs, **SantiagoKwargs)
        SantiagoFin = SantiagoTime.time()
        print(f"Tiempo de ejecución: {SantiagoFin - SantiagoIni:.5f} segundos")
        return SantiagoR
    return SantiagoWrapper

@SantiagoMed
def SantiagoSumN(SantiagoList):
    return sum(SantiagoList)

print(SantiagoSumN(list(range(1000000))))
