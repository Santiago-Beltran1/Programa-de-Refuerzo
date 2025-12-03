import os as SantiagoOs

def SantiagoBusP(SantiagoDirect, SantiagoP):
    SantiagoR = []
    for SantiagoArch in SantiagoOs.listdir(SantiagoDirect):
        SantiagoRuta = SantiagoOs.path.join(SantiagoDirect, SantiagoArch)
        if SantiagoOs.path.isfile(SantiagoRuta):
            with open(SantiagoRuta, "r") as SantiagoF:
                if SantiagoP in SantiagoF.read():
                    SantiagoR.append(SantiagoArch)
    if SantiagoR:
        print(f"Palabra '{SantiagoP}' encontrada en archivos: {SantiagoR}")
    else:
        print(f"Palabra '{SantiagoP}' no encontrada en ningún archivo")

SantiagoBusP(".", "Santiago")
