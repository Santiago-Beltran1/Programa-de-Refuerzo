import re

def SantiagoBValidarTelefono(SantiagoBTelefono):
    if re.fullmatch(r"\+?\d{10,13}", SantiagoBTelefono):
        print("Número de teléfono válido")
    else:
        print("Número inválido")

SantiagoBTelefono = input("Ingrese número de teléfono (+ o sin él, 10-13 dígitos): ")
SantiagoBValidarTelefono(SantiagoBTelefono)
