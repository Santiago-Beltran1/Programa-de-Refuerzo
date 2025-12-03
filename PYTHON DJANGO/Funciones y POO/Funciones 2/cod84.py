import os as SantiagoOs
import hashlib as SantiagoHash

def SantiagoDetect(SantiagoDirect):
    SantiagoHashes = {}
    SantiagoDup = []
    for SantiagoArch in SantiagoOs.listdir(SantiagoDirect):
        SantiagoRuta = SantiagoOs.path.join(SantiagoDirect, SantiagoArch)
        if SantiagoOs.path.isfile(SantiagoRuta):
            with open(SantiagoRuta, "rb") as SantiagoF:
                SantiagoCont = SantiagoF.read()
                SantiagoHashArch = SantiagoHash.md5(SantiagoCont).hexdigest()
                if SantiagoHashArch in SantiagoHashes:
                    SantiagoDup.append(SantiagoArch)
                else:
                    SantiagoHashes[SantiagoHashArch] = SantiagoArch
    if SantiagoDup:
        print(f"Archivos duplicados detectados: {SantiagoDup}")
    else:
        print("No se detectaron duplicados")

SantiagoDetect(".")
