class SantiagoB:
    SantiagoMinC = -273.15 

    def __init__(self, SantiagoCelsius=0):
        self.santiago_celsius = SantiagoCelsius

    @property
    def SantiagoCelsius(self):
        return self.santiago_celsius

    @SantiagoCelsius.setter
    def SantiagoCelsius(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("La temperatura debe ser un número.")
        if valor < self.SantiagoMinC:
            raise ValueError(f"La temperatura no puede ser inferior al cero absoluto ({self.SantiagoMinC}°C).")
        self.santiago_celsius = float(valor)

    @property
    def SantiagoFahrenheit(self):
        return (self.santiago_celsius * 9/5) + 32

    @SantiagoFahrenheit.setter
    def SantiagoFahrenheit(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("La temperatura debe ser un número.")
        self.SantiagoCelsius = (valor - 32) * 5/9  # Reutiliza el setter de Celsius

    def SantiagoMostrar(self):
        return f"Temperatura: {self.santiago_celsius:.2f}°C / {self.SantiagoFahrenheit:.2f}°F"


try:
    santiagoT1 = SantiagoB(30)
    print(santiagoT1.SantiagoMostrar())

    print(f"Temperatura en Celsius: {santiagoT1.SantiagoCelsius:.2f}°C")
    santiagoT1.SantiagoCelsius = 15
    print(santiagoT1.SantiagoMostrar())

    print(f"Temperatura en Fahrenheit: {santiagoT1.SantiagoFahrenheit:.2f}°F")
    santiagoT1.SantiagoFahrenheit = 98.6
    print(santiagoT1.SantiagoMostrar())

except ValueError as e:
    print(f"Error de validación: {e}")
except TypeError as e:
    print(f"Error de tipo: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
