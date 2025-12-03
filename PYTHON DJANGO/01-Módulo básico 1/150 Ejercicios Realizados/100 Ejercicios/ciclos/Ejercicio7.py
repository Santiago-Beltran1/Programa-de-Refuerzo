#Validador de correo

santiagoEmail = input("Ingresa tu correo electrónico: ")
if "@" in santiagoEmail and "." in santiagoEmail and santiagoEmail.index("@") < santiagoEmail.rindex("."):
    print("Email válido.")
else:
    print("Email inválido.")
