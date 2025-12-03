SantiagoInv = {"nevera":7, "lavadora":1, "estufa":15}
SantiagoB = ""
while SantiagoB != "fin":
    SantiagoB = input("Agregar, vender, mostrar o 'fin': ").lower()
    if SantiagoB == "agregar":
        SantiagoProd = input("Producto: ").lower()
        SantiagoCant = int(input("Cantidad: "))
        SantiagoInv[SantiagoProd] = SantiagoInv.get(SantiagoProd,0)+SantiagoCant
    elif SantiagoB == "vender":
        SantiagoProd = input("Producto: ").lower()
        SantiagoCant = int(input("Cantidad: "))
        if SantiagoProd in SantiagoInv and SantiagoInv[SantiagoProd]>=SantiagoCant:
            SantiagoInv[SantiagoProd]-=SantiagoCant
        else:
            print("Stock insuficiente")
    elif SantiagoB == "mostrar":
        for SantiagoProd, SantiagoCant in SantiagoInv.items():
            SantiagoEstd = "Bajo stock" if SantiagoCant < 3 else "Stock suficiente"
            print(SantiagoProd, ":", SantiagoCant, "-", SantiagoEstd)
