#Calculadora de saldo tras gastos mensuales
santiagoIngresos = 1500
santiagoGastos = [300, 150, 200, 400]  

santiagoTotalGastos = 0
for santiagoGasto in santiagoGastos:
    santiagoTotalGastos += santiagoGasto

santiagoSaldo = santiagoIngresos - santiagoTotalGastos
print(f"Saldo restante: ${santiagoSaldo}")
