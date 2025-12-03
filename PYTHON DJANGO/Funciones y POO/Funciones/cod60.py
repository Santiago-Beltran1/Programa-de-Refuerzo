def SantiagoBConvertirCmAPulgadas(SantiagoCm):
    return SantiagoCm / 2.54

SantiagoCm = float(input("Ingresa centímetros: "))
print(f"{SantiagoCm} cm = {SantiagoBConvertirCmAPulgadas(SantiagoCm):.2f} pulgadas")
