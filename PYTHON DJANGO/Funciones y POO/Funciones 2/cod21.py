def SantiagoInvDic(SantiagoDic):
    return {valor: clave for clave, valor in SantiagoDic.items()}

SantiagoDicOriginal = {"SantiagoUno":1, "SantiagoDos":2}
print(SantiagoInvDic(SantiagoDicOriginal))
