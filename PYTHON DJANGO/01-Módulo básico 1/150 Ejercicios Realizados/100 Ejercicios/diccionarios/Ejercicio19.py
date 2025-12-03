#Login con contraseña encriptada

santiagoUsers = {}
santiagoNoms = input("Usuario: ")
santiagoPass = input("Contraseña: ")

santiagoUsers[santiagoNoms] = "*" * len(santiagoPass)
print("Usuarios con contraseña cifrada:", santiagoUsers)
