def SantiagoBuscarNumero(SantiagoList, SantiagoNum):
    return SantiagoNum in SantiagoList

def SantiagoBuscar():
    SantiagoLista = [int(SantiagoX) for SantiagoX in input("Números separados por espacio: ").split()]
    SantiagoNum = int(input("Número a buscar: "))
    print("Encontrado:", SantiagoBuscarNumero(SantiagoLista, SantiagoNum))

SantiagoBuscar()
