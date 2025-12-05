def SantiagoBGrafica(valores):
    for etiqueta, valor in valores.items():
        print(f"{etiqueta}: {'█' * valor}")

SantiagoBValores = {
    "A": 3,
    "B": 7,
    "C": 5,
    "D": 2
}
SantiagoBGrafica(SantiagoBValores)
