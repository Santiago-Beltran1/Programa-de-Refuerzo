def SantiagoBVotacion():
    SantiagoBOpciones = {"A": 0, "B": 0, "C": 0}
    for i in range(5):
        SantiagoBVoto = input("Vota por A, B o C: ").upper()
        if SantiagoBVoto in SantiagoBOpciones:
            SantiagoBOpciones[SantiagoBVoto] += 1
        else:
            print("Voto inválido.")
    print("Resultados:", SantiagoBOpciones)
    SantiagoBGanador = max(SantiagoBOpciones, key=SantiagoBOpciones.get)
    print(f"Ganador: {SantiagoBGanador}")

SantiagoBVotacion()
