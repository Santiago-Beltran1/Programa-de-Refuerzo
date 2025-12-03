import time as SantiagoTime

def SantiagoRelojD(SantiagoSegundos):
    for SantiagoCont in range(SantiagoSegundos):
        SantiagoHora = SantiagoTime.strftime("%H:%M:%S", SantiagoTime.localtime())
        print(f"Hora actual: {SantiagoHora}")
        SantiagoTime.sleep(1)

SantiagoRelojD(5)
