#Cajero con menú de opciones

santiagoSald = 100000

while True:
    print("\n1. Consultar saldo\n2. Retirar dinero\n3. Salir")
    santiagoOp = input("Elija una opción: ")

    if santiagoOp == "1":
        print(f"Saldo actual: ${santiagoSald}")
    elif santiagoOp == "2":
        santiagoRet = int(input("Cantidad a retirar: "))
        if santiagoRet <= santiagoSald:
            santiagoSald -= santiagoRet
            print("Retiro exitoso. Saldo actual:", santiagoSald)
        else:
            print("Saldo insuficiente.")
    elif santiagoOp == "3":
        break
