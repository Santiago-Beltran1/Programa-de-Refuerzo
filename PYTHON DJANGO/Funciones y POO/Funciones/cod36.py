def SantiagoPromedio(SantiagoLista):
    return sum(SantiagoLista) / len(SantiagoLista)

def SantiagoMain():
    try:
        SantiagoDatos = input("Ingresa números separados por coma: ")
        SantiagoNums = [float(x) for x in SantiagoDatos.split(",")]
        print(f"El promedio es: {SantiagoPromedio(SantiagoNums):.2f}")
    except:
        print("Error: Verifica los valores ingresados.")

SantiagoMain()
