#Almacenar resultados de una encuesta de satisfacción

santiagoEncues = {}
for santiagoI in range(3):
    santiagoCli = input("Nombre del cliente: ")
    santiagoCal = int(input("Calificación (1-5): "))
    santiagoEncues[santiagoCli] = santiagoCal

print("Resultados:", santiagoEncues)
