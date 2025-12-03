#Simulador de un retiro

santiagoSal = 50000
while santiagoSal > 0:
    santiagoRet = int(input(f"Saldo: {santiagoSal}. Ingrese monto a retirar: "))
    if santiagoRet <= santiagoSal:
        santiagoSal -= santiagoRet
        print("Retiro exitoso")
    else:
        print("Saldo insuficiente")
print("Saldo agotado")
