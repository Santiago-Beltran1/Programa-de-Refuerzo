# Usuario ingresa 5 números y se ordenan de menor mayor
santiagoNums = tuple(int(input(f"Ingrese número {i+1}: ")) for i in range(5))

santiagoOrden = tuple(sorted(santiagoNums))
print("Números ordenados:", santiagoOrden)
