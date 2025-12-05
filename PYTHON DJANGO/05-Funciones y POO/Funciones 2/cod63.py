import matplotlib.pyplot as SantiagoPlot
import numpy as SantiagoNp

def SantiagoGrafF(SantiagoFunc, SantiagoRng):
    SantiagoX = SantiagoNp.linspace(SantiagoRng[0], SantiagoRng[1], 100)
    SantiagoY = SantiagoFunc(SantiagoX)
    SantiagoPlot.plot(SantiagoX, SantiagoY)
    SantiagoPlot.title("Función Matemática")
    SantiagoPlot.show()

SantiagoGrafF(lambda x: x**2, (0,10))
