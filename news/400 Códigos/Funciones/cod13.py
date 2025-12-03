santiagocont = 0  

def SantiagoB():
    global santiagocont  
    santiagocont += 1
    print(f"Contador dentro de la función: {santiagocont}")

SantiagoB()
SantiagoB()
SantiagoB()
print(f"Contador fuera de la función: {santiagocont}")

