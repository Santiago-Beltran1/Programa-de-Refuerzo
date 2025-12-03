#Simulador de compra y actualización del diccionario

santiagoPrecios = {"Pliego de Craft": 1000, "Pliego de Papel Periódico": 800}
santiagoProd = input("Producto a comprar: ")
santiagoValor = santiagoPrecios.pop(santiagoProd, "No encontrado")
print("Producto eliminado:", santiagoValor)
print("Diccionario ahora:", santiagoPrecios)
