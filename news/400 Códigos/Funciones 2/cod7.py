import matplotlib.pyplot as SantiagoPlot

def SantiagoGrafic(SantiagoEtiquet, SantiagoVals):
    SantiagoPlot.bar(SantiagoEtiquet, SantiagoVals)
    SantiagoPlot.title("Santiago Gráfico de Barras")
    SantiagoPlot.show()

SantiagoNoms = ["SantiagoUno", "SantiagoDos", "SantiagoTres"]
SantiagoPuntjs = [19, 15, 7]
SantiagoGrafic(SantiagoNoms, SantiagoPuntjs)
