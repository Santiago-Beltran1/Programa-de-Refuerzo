import os as SantiagoOs
import time as SantiagoTime

def SantiagoElimTemp(SantiagoDirectorio, SantiagoDias=1):
    SantiagoAhora = SantiagoTime.time()
    for SantiagoArch in SantiagoOs.listdir(SantiagoDirectorio):
        SantiagoRuta = SantiagoOs.path.join(SantiagoDirectorio, SantiagoArch)
        if SantiagoOs.path.isfile(SantiagoRuta):
            if SantiagoAhora - SantiagoOs.path.getmtime(SantiagoRuta) > SantiagoDias*86400:
                SantiagoOs.remove(SantiagoRuta)
                print(f"SantiagoArchivo eliminado: {SantiagoArch}")

SantiagoElimTemp(".")
