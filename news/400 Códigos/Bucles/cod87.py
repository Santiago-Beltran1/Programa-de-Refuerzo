SantiagoEst = ["David", "Santiago", "Beltran"]
SantiagoAsis = {}

for SantiagoB in SantiagoEst:
    SantiagoCont = 0
    for SantiagoDia in range(5):
        SantiagoResp = input(f"{SantiagoB} estuvo presente el día {SantiagoDia+1}? (s/n): ").lower()
        if SantiagoResp == "s":
            SantiagoCont += 1
    SantiagoAsis[SantiagoB] = SantiagoCont

print("\nAsistencias finales:")
for SantiagoEst, SantiagoDias in SantiagoAsis.items():
    print(SantiagoEst, ":", SantiagoDias, "días presentes")
