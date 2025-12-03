import os as SantiagoOs

def SantiagoListArch(SantiagoDir):
    return [SantiagoArch for SantiagoArch in SantiagoOs.listdir(SantiagoDir) if SantiagoOs.path.isfile(SantiagoOs.path.join(SantiagoDir, SantiagoArch))]

print(SantiagoListArch("."))
