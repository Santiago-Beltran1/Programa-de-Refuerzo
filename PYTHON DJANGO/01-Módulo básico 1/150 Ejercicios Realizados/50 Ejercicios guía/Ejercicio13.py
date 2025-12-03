# Sumador acumulativo
santiagoSTotal = 0 
santiagoNAct = 1 
santiagoLimit = 50 

print("Sumando números del 1 al ", santiagoLimit, "...")

while santiagoNAct <= santiagoLimit:
    santiagoSTotal = santiagoSTotal + santiagoNAct 
    print("Sumando ", santiagoNAct, "- Total hasta ahora: ", santiagoSTotal)
    santiagoNAct = santiagoNAct + 1
    
print("\nResultado final:")
print("La suma de todos los números del 1 al", santiagoLimit, "es:", santiagoSTotal)