SantiagoEST = [
    {"nombre": "David", "nota": 15},
    {"nombre": "Santiago", "nota": 42},
    {"nombre": "Beltran", "nota": 89}
]

SantiagoOrden = sorted(SantiagoEST, key=lambda Santiagoe: Santiagoe["nota"], reverse=True)
print(SantiagoOrden)
