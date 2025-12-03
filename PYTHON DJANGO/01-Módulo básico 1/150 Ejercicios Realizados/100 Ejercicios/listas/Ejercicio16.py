#Encuesta

santiagoResp = []

for santiagoI in range(5):
    santiagoR = input("¿Te gusta la salchipapa? (si/no): ")
    santiagoResp.append(santiagoR.lower())

print("Resultados de la encuesta:")
print("Sí:", santiagoResp.count("si"))
print("No:", santiagoResp.count("no"))
