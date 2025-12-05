def SantiagoB(Santiagotxt):
    Santiagovoc = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    Santiagocont = sum(1 for Santiagol in Santiagotxt if Santiagol in Santiagovoc)
    print(f"La frase '{Santiagotxt}' tiene {Santiagocont} vocales.")
    return Santiagocont

SantiagoB("David Santiago Beltran Pedraza")