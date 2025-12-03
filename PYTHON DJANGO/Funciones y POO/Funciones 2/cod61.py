import csv as SantiagoCsv

class SantiagoG:
    def __init__(self, SantiagoDesc, SantiagoMonto):
        self.SantiagoDescripcion = SantiagoDesc
        self.SantiagoMonto = SantiagoMonto

class SantiagoRegis:
    def __init__(self):
        self.SantiagoGastos = []

    def SantiagoAg(self, SantiagoGastoI):
        self.SantiagoGastos.append(SantiagoGastoI)

    def SantiagoExpCSV(self, SantiagoArch):
        with open(SantiagoArch, "w", newline="") as SantiagoF:
            SantiagoCampos = ["Descripcion","Monto"]
            SantiagoWriter = SantiagoCsv.DictWriter(SantiagoF, fieldnames=SantiagoCampos)
            SantiagoWriter.writeheader()
            for DavidG in self.SantiagoGastos:
                SantiagoWriter.writerow({"SantiagoDescripcion":DavidG.SantiagoDescripcion, "SantiagoMonto":DavidG.SantiagoMonto})

SantiagoReg = SantiagoRegis()
SantiagoReg.SantiagoAg(SantiagoG("Comida", 150000))
SantiagoReg.SantiagoAg(SantiagoG("Transporte", 150000))
# SantiagoReg.SantiagoExportarCSV("SantiagoGastos.csv")
