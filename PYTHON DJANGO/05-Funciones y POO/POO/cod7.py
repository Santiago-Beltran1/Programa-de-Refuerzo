class SantiagoPulpo:
    def SantiagoSon(self):
        return "El pulpo emite burbujas"

    def SantiagoNadar(self):
        return "El pulpo está nadando ágilmente entre los corales"

    def SantiagoCambiar(self):
        return "El pulpo cambia de color para camuflarse"


class SantiagoHumano:
    def SantiagoSon(self):
        return "¡Hola!"

    def SantiagoNadar(self):
        return "La persona está nadando"


class SantiagoRobot:
    def SantiagoSon(self):
        return "Beep boop"

    def SantiagoNadar(self):
        return "El robot está flotando"


def SantiagoActividadEnPiscina(participante):
    print(participante.SantiagoNadar())
    print(f"Dice: {participante.SantiagoSon()}")
    if hasattr(participante, "SantiagoCambiarColor"):
        print(participante.SantiagoCambiar())


santiagoPulpo = SantiagoPulpo()
santiagoPerson = SantiagoHumano()
santiagoRobot = SantiagoRobot()

print("=== DÍA EN LA PISCINA SANTIAGO ===\n")
SantiagoActividadEnPiscina(santiagoPulpo)
print()
SantiagoActividadEnPiscina(santiagoPerson)
print()
SantiagoActividadEnPiscina(santiagoRobot)
