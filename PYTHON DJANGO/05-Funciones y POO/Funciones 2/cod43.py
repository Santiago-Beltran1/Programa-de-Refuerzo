import matplotlib.pyplot as SantiagoPlot
import numpy as SantiagoNp

def SantiagoAumPob(SantiagoInicial, SantiagoTasa, SantiagoDias):
    SantiagoDiasArr = SantiagoNp.arange(SantiagoDias)
    SantiagoPoblacion = SantiagoInicial * (1 + SantiagoTasa) ** SantiagoDiasArr
    SantiagoPlot.plot(SantiagoDiasArr, SantiagoPoblacion)
    SantiagoPlot.title("Crecimiento Poblacional")
    SantiagoPlot.show()

SantiagoAumPob(150, 0.1, 20)
