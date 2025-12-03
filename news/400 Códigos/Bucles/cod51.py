SantiagoB = "Amor a Roma"
SantiagoVacio = SantiagoB.replace(" ", "").lower()
SantiagoRever = ""

for SantiagoL in SantiagoVacio:
    SantiagoRever = SantiagoL + SantiagoRever

print(f"La frase '{SantiagoB}' es palíndromo:", SantiagoVacio == SantiagoRever)
