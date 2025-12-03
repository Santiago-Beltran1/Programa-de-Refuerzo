import json as SantiagoJson

def SantiagoJsonDic(SantiagoJsonString):
    return SantiagoJson.loads(SantiagoJsonString)

Santiago = '{"Nombre":"David Beltran","Nivel":"3 Trimestre"}'
print(SantiagoJsonDic(Santiago))
