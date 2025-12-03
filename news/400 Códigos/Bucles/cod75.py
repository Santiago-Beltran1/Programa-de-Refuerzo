SantiagoB = []
while True:
    SantiagoNom = input("Nombre del empleado (o 'fin' para terminar): ")
    if SantiagoNom.lower() == "fin":
        break
    SantiagoH = int(input("Horas trabajadas: "))
    SantiagoPago = float(input("Pago por hora: "))
    SantiagoSal = SantiagoH * SantiagoPago
    SantiagoB.append({"nombre": SantiagoNom, "salario": SantiagoSal})

print("\nSalarios calculados:")
for SantiagoE in SantiagoB:
    print(f"{SantiagoE['nombre']}: ${SantiagoE['salario']}")
