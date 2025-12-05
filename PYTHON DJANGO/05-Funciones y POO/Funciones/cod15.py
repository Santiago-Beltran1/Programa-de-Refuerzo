def SantiagoB(santiagoProduct, santiagoCant=1, santiagodesc=0, santiagoImps=0.21):
    SantiagoBase = santiagoProduct * santiagoCant
    SantiagoPCD = SantiagoBase * (1 - santiagodesc)
    SantiagoFinal = SantiagoPCD * (1 + santiagoImps)
    return SantiagoFinal


santiago1 = SantiagoB(100)                                 
santiago2 = SantiagoB(100, 2)                              
santiago3 = SantiagoB(100, santiagodesc=0.1)                 
santiago4 = SantiagoB(santiagoProduct=100, santiagoImps=0.10)        