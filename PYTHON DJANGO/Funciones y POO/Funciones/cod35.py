def SantiagoB_Tabla(SantiagoNum):
    for SantiagoI in range(1, 11):
        print(f"{SantiagoNum} x {SantiagoI} = {SantiagoNum * SantiagoI}")

def SantiagoB():
    try:
        SantiagoNum = int(input("Ingresa un número para generar tu tabla: "))
        SantiagoB_Tabla(SantiagoNum)
    except ValueError:
        print("Ingresa un número válido.")

SantiagoB()
