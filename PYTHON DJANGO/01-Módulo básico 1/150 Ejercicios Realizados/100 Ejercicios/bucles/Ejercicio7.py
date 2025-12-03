#Encontrar el número dentro de cierto radio hasta acertar

import random
santiagoN = random.randint(1,10)

while True:
    santiagoInt = int(input("Adivine el número (1-10): "))
    if santiagoInt == santiagoN:
        print("¡Has Acertado!, el número es: ", santiagoN)
        break
    elif santiagoInt < santiagoN:
        print("Muy bajo")
    else:
        print("Muy alto")
