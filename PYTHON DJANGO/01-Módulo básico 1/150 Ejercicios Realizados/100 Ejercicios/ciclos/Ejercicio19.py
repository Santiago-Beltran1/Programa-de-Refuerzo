#Conversión de moneda

santiagoUSD = 0.00025  
santiagoCOP = 4000    

santiagoOp = input("Elija conversión (1: USD a COP, 2: COP a USD): ").lower()

if santiagoOp == "1":
    santiagousd = float(input("Ingrese cantidad en USD: "))
    santiagocop = santiagousd * santiagoCOP
    print(f"{santiagousd} USD son {santiagocop:.2f} COP")
elif santiagoOp == "2":
    santiagocop = float(input("Ingrese cantidad en COP: "))
    santiagousd = santiagocop * santiagoUSD
    print(f"{santiagocop} COP son {santiagousd:.2f} USD")
else:
    print("Opción inválida, elija 1 o 2.")
