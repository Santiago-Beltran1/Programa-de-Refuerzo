#Calculadora de impuestos

santiagoIngresos = float(input("Ingrese ingresos anuales: "))

if santiagoIngresos < 10000:
    print("No paga impuestos")
elif santiagoIngresos < 50000:
    santiagoImpuestos = santiagoIngresos * 0.10
    print(f"Paga 10% de impuestos, es decir: {santiagoImpuestos:.2f}")
else:
    santiagoImpuestos = santiagoIngresos * 0.20
    print(f"Paga 20% de impuestos, es decir: {santiagoImpuestos:.2f}")
