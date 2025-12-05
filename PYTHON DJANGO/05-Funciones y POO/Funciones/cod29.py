def SantiagoB_Decorador(SantiagoFunc):
    def Santiago_wrapper():
        print("Antes de llamar a la función")
        SantiagoFunc()
        print("Después de llamar a la función")
    return Santiago_wrapper

@SantiagoB_Decorador
def SantiagoSaluda():
    print("¡Hola!")

SantiagoSaluda()
