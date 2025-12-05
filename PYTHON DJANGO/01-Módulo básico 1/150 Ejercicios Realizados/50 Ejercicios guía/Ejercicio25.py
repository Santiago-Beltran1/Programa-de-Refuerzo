# Sistema de registro de estudiantes

santiagoEsts = []  # Lista global para almacenar estudiantes

def santiagoAgEst(santiagoNom, santiagoEdad, santiagoGrado):
    """Agrega un nuevo estudiante al sistema"""
    estudiante = {
        "nombre": santiagoNom,
        "edad": santiagoEdad,
        "grado": santiagoGrado,
        "calificaciones": []
    }
    santiagoEsts.append(estudiante)
    print(f"Estudiante {santiagoNom} agregado exitosamente")

def santiagoBus(nombre):
    """Busca un estudiante por nombre"""
    for i, estudiante in enumerate(santiagoEsts):
        if estudiante["nombre"].lower() == nombre.lower():
            return i  # Retorna la posición
    return -1  # No encontrado

def santiagoAgCal(santiagoNom, santiagoMat, santiagoNota):
    """Agrega una calificación a un estudiante"""
    santiagoPos = santiagoBus(santiagoNom)
    if santiagoPos != -1:
        santiagoCal = {"materia": santiagoMat, "nota": santiagoNota}
        santiagoEsts[santiagoPos]["calificaciones"].append(santiagoCal)
        print(f"Calificación agregada a {santiagoNom}: {santiagoMat} = {santiagoNota}")
    else:
        print(f"Estudiante {santiagoNom} no encontrado")

def santiagoCalcProm(santiagoNom):
    """Calcula el promedio de un estudiante"""
    santiagoPos = santiagoBus(santiagoNom)
    if santiagoPos != -1:
        santiagoCal = santiagoEsts[santiagoPos]["calificaciones"]
        if santiagoCal:
            suma = sum(cal["nota"] for cal in santiagoCal)
            promedio = suma / len(santiagoCal)
            return round(promedio, 2)
        else:
            return 0
    return None

def santiagoMosReport():
    """Muestra un reporte completo de todos los estudiantes"""
    print("\n" + "=" * 50)
    print("REPORTE DE ESTUDIANTES")
    print("=" * 50)
    for estudiante in santiagoEsts:
        print(f"\nNombre: {estudiante['nombre']}")
        print(f"Edad: {estudiante['edad']} años")
        print(f"Grado: {estudiante['grado']}")
        if estudiante["calificaciones"]:
            print("Calificaciones:")
            for cal in estudiante["calificaciones"]:
                print(f" - {cal['materia']}: {cal['nota']}")
            promedio = santiagoCalcProm(estudiante['nombre'])
            print(f"Promedio general: {promedio}")
        else:
            print("Sin calificaciones registradas")
        print("-" * 30)

print("SISTEMA DE REGISTRO DE ESTUDIANTES")

# Agregar estudiantes
santiagoAgEst("David Santiago", 16, "10°")
santiagoAgEst("Santiago Beltran", 15, "9°")
santiagoAgEst("David Pedraza", 17, "11°")

# Agregar calificaciones
santiagoAgCal("David Santiago", "Matemáticas", 9.2)
santiagoAgCal("David Santiago", "Historia", 8.8)
santiagoAgCal("David Santiago", "Ciencias", 9.5)

santiagoAgCal("Santiago Beltran", "Matemáticas", 7.5)
santiagoAgCal("Santiago Beltran", "Historia", 8.2)

santiagoAgCal("Pedro Martín", "Matemáticas", 8.0)  # Este no existe

# Mostrar reporte
santiagoMosReport()
