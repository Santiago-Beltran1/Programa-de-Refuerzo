import matplotlib.pyplot as SantiagoPlot
import numpy as SantiagoNp

def SantiagoGraficoDiS(SantiagoPnts):
    SantiagoX = SantiagoNp.random.rand(SantiagoPnts)
    SantiagoY = SantiagoNp.random.rand(SantiagoPnts)
    SantiagoPlot.scatter(SantiagoX, SantiagoY)
    SantiagoPlot.title("Gráfico de Dispersión")
    SantiagoPlot.show()

SantiagoGraficoDiS(31)
