# Calculadora con funciones
def santiagoSum(a, b):
    """Suma dos números y devuelve el resultado"""
    resultado = a + b
    return resultado

def santiagoRes(a, b):
    """Resta b de a y devuelve el resultado"""
    resultado = a - b
    return resultado

def santiagoMul(a, b):
    """Multiplica dos números y devuelve el resultado"""
    resultado = a * b
    return resultado

def santiagoDiv(a, b):
    """Divide a entre b y devuelve el resultado"""
    if b != 0: 
        resultado = a / b
        return resultado
    else:
        return "Error: No se puede dividir entre cero"
    

santiagoN1 = float(input("Ingrese el primer número"))
santiagoN2 = float(input("Ingrese el segundo número"))

print("CALCULADORA CON FUNCIONES")
print(f"Números a operar: {santiagoN1} y {santiagoN2}")
print("-" * 30)

print(f"{santiagoN1} + {santiagoN2} = {santiagoSum(santiagoN1, santiagoN2)}")
print(f"{santiagoN1} - {santiagoN2} = {santiagoRes(santiagoN1, santiagoN2)}")
print(f"{santiagoN1} * {santiagoN2} = {santiagoMul(santiagoN1, santiagoN2)}")
print(f"{santiagoN1} / {santiagoN2} = {santiagoDiv(santiagoN1, santiagoN2)}")

# Probando división entre cero
print(f"{santiagoN1} / 0 = {santiagoDiv(santiagoN1, 0)}")
