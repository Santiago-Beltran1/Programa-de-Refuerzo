#EJERCICIOS FINALES - Gestor de biblioteca

santiagoBiblioteca = {
    "libros": [],
    "usuarios": [],
    "prestamos": []
}

def santiagoAgLibro(santiagoTitulo):
    santiagoBiblioteca["libros"].append(santiagoTitulo)

def santiagoAgUsur(santiagoNom):
    santiagoBiblioteca["usuarios"].append(santiagoNom)

def santiagoPrestar(santiagoLib, santiagoUser):
    if santiagoLib in santiagoBiblioteca["libros"] and santiagoUser in santiagoBiblioteca["usuarios"]:
        santiagoBiblioteca["prestamos"].append((santiagoLib, santiagoUser))
        print(f"{santiagoLib} prestado a {santiagoUser}")
    else:
        print("Libro o usuario no registrado")

# Ejemplo
santiagoAgLibro("Luna de Plutón")
santiagoAgUsur("Santiago")
santiagoPrestar("Luna de Plutón", "Santiago")
print(santiagoBiblioteca)
