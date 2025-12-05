def SantiagoB_Hasta(SantiagoN):
    """Generador que produce números del 1 al n."""
    Santiagoi = 1
    while Santiagoi <= SantiagoN:
        yield Santiagoi
        Santiagoi += 1

for SantiagoNum in SantiagoB_Hasta(15):
    print(SantiagoNum, end=" ") 
