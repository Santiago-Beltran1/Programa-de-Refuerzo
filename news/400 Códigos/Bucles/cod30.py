import os

SantiagoB_Direct = './imagenes'

for SantiagoI, SantiagoArch in enumerate(os.listdir(SantiagoB_Direct)):
    if SantiagoArch.endswith('.jpg'):
        SantiagoNew = f'foto_{SantiagoI}.jpg'
        SantiagoRutaAct = os.path.join(SantiagoB_Direct, SantiagoArch)
        SantiagoRutaNew = os.path.join(SantiagoB_Direct, SantiagoNew)
        os.rename(SantiagoRutaAct, SantiagoRutaNew)
