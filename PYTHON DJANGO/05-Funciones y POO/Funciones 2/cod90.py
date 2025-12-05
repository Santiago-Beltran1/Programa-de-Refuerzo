import time as SantiagoTime

def SantiagoTemp(SantiagoTiempos):
    for SantiagoNom, SantiagoSeg in SantiagoTiempos.items():
        print(f"Temporizador iniciado: {SantiagoNom} por {SantiagoSeg} segundos")
        SantiagoTime.sleep(SantiagoSeg)
        print(f"ALERTA: {SantiagoNom} finalizado después de {SantiagoSeg} segundos")

SantiagoTemp({"Limpiar la cocina":2, "Gym":3})
