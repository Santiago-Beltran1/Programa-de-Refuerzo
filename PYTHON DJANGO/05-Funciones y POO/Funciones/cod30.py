import time

def SantiagoB_Medir(SantiagoFunc):
    def Santiago_wrapper(*Santiago_args, **Santiago_kwargs):
        SantiagoInicio = time.time()
        SantiagoR = SantiagoFunc(*Santiago_args, **Santiago_kwargs)
        SantiagoFin = time.time()
        print(f"La función {SantiagoFunc.__name__} tardó {SantiagoFin - SantiagoInicio:.5f} segundos en ejecutarse")
        return SantiagoR
    return Santiago_wrapper

@SantiagoB_Medir
def SantiagoSum():
    return sum(range(1000000))

# Llamada a la función decorada
SantiagoR = SantiagoSum()
print(f"Resultado: {SantiagoR}")
