import json as SantiagoJSON

def SantiagoJSON(SantiagoArch):
    with open(SantiagoArch, "r") as SantiagoF:
        SantiagoData = SantiagoJSON.load(SantiagoF)
    print(f"Contenido de {SantiagoArch}:")
    for SantiagoClave, SantiagoVal in SantiagoData.items():
        print(f"  {SantiagoClave}: {SantiagoVal}")

SantiagoJSON("SantiagoDatos.json")
