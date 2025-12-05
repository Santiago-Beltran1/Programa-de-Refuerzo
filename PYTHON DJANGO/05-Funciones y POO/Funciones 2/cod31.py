import csv as SantiagoCsv

def SantiagoCSV(SantiagoNom, SantiagoDatos):
    with open(SantiagoNom, "w", newline="") as SantiagoArch:
        SantiagoCampos = SantiagoDatos[0].keys()
        SantiagoEscritor = SantiagoCsv.DictWriter(SantiagoArch, fieldnames=SantiagoCampos)
        SantiagoEscritor.writeheader()
        SantiagoEscritor.writerows(SantiagoDatos)
    return f"{SantiagoNom} creado"

SantiagoListaDic = [{"Nombre":"David","Nivel":"T3"},{"Nombre":"Santiago","Nivel":"T2"}]
print(SantiagoCSV("SantiagoDatos.csv", SantiagoListaDic))
