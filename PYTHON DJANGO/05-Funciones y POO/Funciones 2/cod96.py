def SantiagoCalorias(SantiagoPeso, SantiagoAlt, SantiagoEdad, SantiagoGen, SantiagoAct):
    if SantiagoGen.lower()=="hombre":
        SantiagoBMR = 10*SantiagoPeso + 6.25*SantiagoAlt - 5*SantiagoEdad + 5
    else:
        SantiagoBMR = 10*SantiagoPeso + 6.25*SantiagoAlt - 5*SantiagoEdad - 161
    SantiagoFactor = {"baja":1.2,"media":1.55,"alta":1.9}.get(SantiagoAct,1.2)
    SantiagoCalorias = SantiagoBMR * SantiagoFactor
    print(f"Calorías diarias recomendadas: {int(SantiagoCalorias)} kcal")

SantiagoCalorias(70,171,25,"hombre","media")
