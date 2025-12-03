def SantiagoB_Dup(SantiagoFacto):
    def SantiagoMul(SantiagoX):
        return SantiagoX * SantiagoFacto
    return SantiagoMul

duplicar = SantiagoB_Dup(2)
print(duplicar(55)) 
