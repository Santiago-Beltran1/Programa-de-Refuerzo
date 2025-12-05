def SantiagoB_Operacion(SantiagoOperacion):
    def SantiagoSum(SantiagoA, SantiagoB):
        return SantiagoA + SantiagoB

    def SantiagoRes(SantiagoA, SantiagoB):
        return SantiagoA - SantiagoB

    if SantiagoOperacion == "suma":
        return SantiagoSum
    elif SantiagoOperacion == "resta":
        return SantiagoRes

f_suma = SantiagoB_Operacion("suma")
print(f_suma(45, 7))  
