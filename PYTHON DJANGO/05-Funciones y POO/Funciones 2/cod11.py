from datetime import datetime as SantiagoDatetime, timedelta as SantiagoDelta

def SantiagoFF(SantiagoDias):
    SantiagoHoy = SantiagoDatetime.now()
    SantiagoFuturo = SantiagoHoy + SantiagoDelta(days=SantiagoDias)
    return SantiagoFuturo

print(f"Serán las: {SantiagoFF(10)}")
