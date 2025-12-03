#Calculadora

santiagoList=["suma", "resta", "multiplicar", "dividir"]

santiagoIng = (int(input("ingrese el numero (1=suma 2=resta 3=multiplicar 4=dividir: ")))
santiagoN1 =(float(input("ingrese el primer numero: ")))
santiagoN2 =(float(input("ingrese el segundo numero: ")))

if santiagoIng == 1:
    print("Usted eligió: ", santiagoList[0])
    print("Resultado de la operación: ", santiagoN1+santiagoN2)
else:
    if santiagoIng == 2:
        print("Usted eligió: ", santiagoList[1])
        print("Resultado de la operación: ", santiagoN1-santiagoN2)
    else:
        if santiagoIng == 3:
            print("Usted eligió: ", santiagoList[2])
            print("Resultado de la operación: ", santiagoN1*santiagoN2)
        else:
            if santiagoIng == 4:
                print("Usted eligió: ", santiagoList[3])
                print("Resultado de la operación: ", santiagoN1/santiagoN2)