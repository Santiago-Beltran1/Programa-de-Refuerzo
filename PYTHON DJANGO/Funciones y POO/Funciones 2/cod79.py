class SantiagoR:
    def __init__(self):
        self.SantiagoReservas = []

    def SantiagoHacer(self, SantiagoNombre, SantiagoFecha):
        if SantiagoFecha in [r["fecha"] for r in self.SantiagoReservas]:
            print(f"SantiagoFecha {SantiagoFecha} ya reservada")
        else:
            self.SantiagoReservas.append({"nombre":SantiagoNombre, "fecha":SantiagoFecha})
            print(f"SantiagoReserva exitosa: {SantiagoNombre} para {SantiagoFecha}")

Santiago1 = SantiagoR()
Santiago1.SantiagoHacer("Santiago", "2025-10-20")
Santiago1.SantiagoHacer("David", "2025-10-20")
Santiago1.SantiagoHacer("Beltran", "2025-10-21")
