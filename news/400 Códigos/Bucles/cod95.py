SantiagoB = ["David","Santiago","Beltran","Pedraza"]
SantiagoAsis = {}
SantiagoI = 0

while SantiagoI < len(SantiagoB):
    SantiagoPres = 0
    for SantiagoDia in range(3):
        SantiagoResp = input(f"{SantiagoB[SantiagoI]} presente día {SantiagoDia+1}? (s/n): ").lower()
        if SantiagoResp == "s":
            SantiagoPres += 1
    SantiagoAsis[SantiagoB[SantiagoI]] = SantiagoPres
    if SantiagoPres < 3:
        print(f"Alerta: {SantiagoB[SantiagoI]} asistencia baja")
    SantiagoI += 1

print(f"Registro final: {SantiagoAsis}")
