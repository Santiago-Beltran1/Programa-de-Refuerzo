#Convertir minutos a horas y minutos

def santiagoaHoras(santiagoMins):
    santiagoH = santiagoMins // 60
    santiagoMinsRes = santiagoMins % 60
    return f"{santiagoH} horas y {santiagoMinsRes} minutos"

print("125 minutos son: ", santiagoaHoras(125))  
