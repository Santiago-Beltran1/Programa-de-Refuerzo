import matplotlib.pyplot as SantiagoPlot
import numpy as SantiagoNp

def SantiagoGraficoLineas(SantiagoPnts):
    SantiagoX = SantiagoNp.arange(SantiagoPnts)
    SantiagoY = SantiagoNp.random.randint(0, 50, SantiagoPnts)
    SantiagoPlot.plot(SantiagoX, SantiagoY)
    SantiagoPlot.title("Santiago Gráfico de Línea Aleatorio")
    SantiagoPlot.show()

SantiagoGraficoLineas(5)
