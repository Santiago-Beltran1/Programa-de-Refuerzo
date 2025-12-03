# Mi primera función
def santiagoSal(santiagoNom): 
    """Esta función saluda a una persona por su nombre"""
    santiagoMens = f"¡Hola {santiagoNom}! ¿Cómo estás?"
    return santiagoMens

# Usar la función (llamarla)
santiagoSal1 = santiagoSal("David") 
santiagoSal2 = santiagoSal("Santiago")
santiagoSal3 = santiagoSal("Beltran") 

print("Usando mi función de saludo:")
print(santiagoSal1)
print(santiagoSal2)
print(santiagoSal3)

# También podemos usarla directamente
print("\nUsando directamente:")
print(santiagoSal("Santiago"))
print(santiagoSal("Beltran"))
