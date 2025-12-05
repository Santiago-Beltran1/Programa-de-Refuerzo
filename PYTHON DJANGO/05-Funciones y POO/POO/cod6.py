class SantiagoBRec:
    def __init__(self, SantiagoLargo, SantiagoAncho):
        if SantiagoLargo > 0 and SantiagoAncho > 0:
            self.santiago_largo = SantiagoLargo
            self.santiago_ancho = SantiagoAncho
        else:
            raise ValueError("El largo y el ancho deben ser valores positivos.")

    def SantiagoArea(self):
        return self.santiago_largo * self.santiago_ancho

    def SantiagoPeri(self):
        return 2 * (self.santiago_largo + self.santiago_ancho)

    def SantiagoDimensiones(self):
        return f"Rectángulo con Largo: {self.santiago_largo} unidades, Ancho: {self.santiago_ancho} unidades."


try:
    santiagoR1 = SantiagoBRec(12, 8)
    print(santiagoR1.SantiagoDimensiones())
    print(f"Área: {santiagoR1.SantiagoArea()} unidades cuadradas.")
    print(f"Perímetro: {santiagoR1.SantiagoPeri()} unidades.")

    santiagoR2 = SantiagoBRec(9, 4.5)
    print(santiagoR2.SantiagoDimensiones())
    print(f"Área: {santiagoR2.SantiagoArea()} unidades cuadradas.")
    print(f"Perímetro: {santiagoR2.SantiagoPeri()} unidades.")

    santiagoR3 = SantiagoBRec(-6, 3)
except ValueError as e:
    print(f"Error al crear rectángulo: {e}")
