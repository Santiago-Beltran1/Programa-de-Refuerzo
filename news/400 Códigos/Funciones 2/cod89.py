import csv as SantiagoCSV

def SantiagoFact(SantiagoCliente, SantiagoItems, SantiagoArch="SantiagoFactura.csv"):
    with open(SantiagoArch, "w", newline="") as SantiagoF:
        SantiagoWriter = SantiagoCSV.writer(SantiagoF)
        SantiagoWriter.writerow(["Producto","Cantidad","Precio","Total"])
        SantiagoTot = 0
        for producto, cantidad, precio in SantiagoItems:
            SantiagoTotal = cantidad * precio
            SantiagoWriter.writerow([producto, cantidad, precio, SantiagoTotal])
            SantiagoTot += SantiagoTotal
    print(f"Factura generada para {SantiagoCliente} con total: ${SantiagoTot}")

SantiagoFact("Santiago",[("Balón",5,2),("Pantaloneta",3,5)])
