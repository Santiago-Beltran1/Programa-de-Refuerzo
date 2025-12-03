SantiagoBEmp = int(input("Ingrese cantidad de empleados: "))
for SantiagoI in range(SantiagoBEmp):
    SantiagoNom = input("Nombre del empleado: ")
    SantiagoHor = int(input("Horas trabajadas: "))
    SantiagoPxH = float(input("Pago por hora: "))
    SantiagoSalario = SantiagoHor * SantiagoPxH
    print(f"El salario de {SantiagoNom} es: ${SantiagoSalario}")
