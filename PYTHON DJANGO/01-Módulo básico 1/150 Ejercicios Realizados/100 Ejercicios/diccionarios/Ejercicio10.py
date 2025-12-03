#Imprimir temperatura de municipio y convertirlo a grados Fahrenheit

santiagoTemps = {"Mosquera": 18, "Funza": 22, "Madrid": 10}
santiagoCitys = input("Ciudad: ")
if santiagoCitys in santiagoTemps:
    print("Temperatura en °C:", santiagoTemps[santiagoCitys])
    print("En °F:", santiagoTemps[santiagoCitys] * 9/5 + 32)
else:
    print("No tengo esa ciudad.")
