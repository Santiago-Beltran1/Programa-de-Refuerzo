import matplotlib.pyplot as SantiagoPlot
import numpy as SantiagoNp

def SantiagoMovPar(SantiagoPasos):
    SantiagoX = [0]
    SantiagoY = [0]
    for _ in range(SantiagoPasos):
        SantiagoX.append(SantiagoX[-1] + SantiagoNp.random.randn())
        SantiagoY.append(SantiagoY[-1] + SantiagoNp.random.randn())
    SantiagoPlot.plot(SantiagoX, SantiagoY)
    SantiagoPlot.title("Movimiento Partícula")
    SantiagoPlot.show()

SantiagoMovPar(35)
