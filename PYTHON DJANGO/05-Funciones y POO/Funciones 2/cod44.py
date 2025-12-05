import time as SantiagoTime

def SantiagoContEvent(SantiagoEvent, SantiagoInter):
    for SantiagoCont in range(SantiagoEvent):
        print(f"Evento {SantiagoCont+1}")
        SantiagoTime.sleep(SantiagoInter)

SantiagoContEvent(5, 3)
