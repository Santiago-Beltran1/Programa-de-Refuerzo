def SantiagoB_CaF(Santiago_celsius):
    """Convierte de Celsius a Fahrenheit."""
    return (Santiago_celsius * 9/5) + 32

def SantiagoB_FaC(Santiago_fahrenheit):
    """Convierte de Fahrenheit a Celsius."""
    return (Santiago_fahrenheit - 32) * 5/9

def SantiagoB_CaK(Santiago_celsius):
    """Convierte de Celsius a Kelvin."""
    return Santiago_celsius + 273.15

def SantiagoB_KaC(Santiago_kelvin):
    """Convierte de Kelvin a Celsius."""
    return Santiago_kelvin - 273.15

SantiagoTemp_Celsius = 10
print(f"{SantiagoTemp_Celsius}°C = {SantiagoB_CaF(SantiagoTemp_Celsius):.2f}°F")
print(f"{SantiagoTemp_Celsius}°C = {SantiagoB_CaK(SantiagoTemp_Celsius):.2f}K")
