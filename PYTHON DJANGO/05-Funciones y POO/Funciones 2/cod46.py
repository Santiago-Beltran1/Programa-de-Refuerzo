import matplotlib.pyplot as SantiagoPlot

def SantiagoGraficCirc(SantiagoCat, SantiagoVals):
    SantiagoPlot.pie(SantiagoVals, labels=SantiagoCat, autopct="%1.1f%%")
    SantiagoPlot.title("Distribución Circular")
    SantiagoPlot.show()

SantiagoCategorias = ["SantiagoA", "SantiagoB", "SantiagoC"]
SantiagoValores = [40, 25, 35]
SantiagoGraficCirc(SantiagoCategorias, SantiagoValores)
