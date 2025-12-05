class SantiagoB:
    def __init__(self, Santiago):
        self.Santiago = Santiago

    def SantiagoPalin(self, SantiagoTexto):
        SantiagoTexto = SantiagoTexto.replace(" ", "").lower()
        return SantiagoTexto == SantiagoTexto[::-1]

Santiago1 = SantiagoB("Verificador de palabra palíndromo")
print(f"La palabra oro es palíndromo: {Santiago1.SantiagoPalin("oro")}")
print(f"La palabra azul es palíndromo: {Santiago1.SantiagoPalin("azul")}")
