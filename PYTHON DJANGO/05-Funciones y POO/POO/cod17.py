class SantiagoBInstrumento:
    def __init__(self, SantiagoTipo):
        self.santiago_tipo = SantiagoTipo  # Tipo de instrumento

    def SantiagoTocar(self):
        return f"El {self.santiago_tipo} está produciendo un sonido genérico."

    def SantiagoAfinar(self):
        return f"Afinando el {self.santiago_tipo}."

    def SantiagoInfo(self):
        return f"Este es un instrumento de tipo {self.santiago_tipo}."


class SantiagoTambor(SantiagoBInstrumento):
    def __init__(self, SantiagoDiametro, SantiagoMarca):
        super().__init__("Tambor")
        self.santiago_diametro = SantiagoDiametro  
        self.santiago_marca = SantiagoMarca       

    def SantiagoTocar(self):
        return f"El tambor {self.santiago_marca} de {self.santiago_diametro} cm suena con ritmo potente."

    def SantiagoGolpear(self):
        return f"Golpeando el tambor {self.santiago_marca}."

    def SantiagoInfo(self):
        return f"{super().SantiagoInfo()}, Marca: {self.santiago_marca}, Diámetro: {self.santiago_diametro} cm."


class SantiagoFlauta(SantiagoBInstrumento):
    def __init__(self, SantiagoMaterial, SantiagoTipo):
        super().__init__("Flauta")
        self.santiago_material = SantiagoMaterial  
        self.santiago_tipo = SantiagoTipo          

    def SantiagoTocar(self):
        return f"La flauta {self.santiago_tipo} de {self.santiago_material} emite una melodía suave."

    def SantiagoLimpiar(self):
        return f"Limpieza realizada en la flauta {self.santiago_tipo}."

    def SantiagoInfo(self):
        return f"{super().SantiagoInfo()}, Material: {self.santiago_material}, Tipo: {self.santiago_tipo}."


santiagoInst = SantiagoBInstrumento("Genérico")
print(santiagoInst.SantiagoInfo())
print(santiagoInst.SantiagoTocar())
print(santiagoInst.SantiagoAfinar())

santiagoT1 = SantiagoTambor(40, "Pearl")
print(santiagoT1.SantiagoInfo())
print(santiagoT1.SantiagoTocar())
print(santiagoT1.SantiagoAfinar())
print(santiagoT1.SantiagoGolpear())

santiagoF1 = SantiagoFlauta("Madera", "Traversa")
print(santiagoF1.SantiagoInfo())
print(santiagoF1.SantiagoTocar())
print(santiagoF1.SantiagoAfinar())
print(santiagoF1.SantiagoLimpiar())
