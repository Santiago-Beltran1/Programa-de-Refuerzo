class SantiagoBInv:
    def __init__(self):
        self.santiago_items = {}

    def SantiagoAddItem(self, SantiagoProducto, SantiagoCantidad):
        if not isinstance(SantiagoProducto, str) or not SantiagoProducto.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        if not isinstance(SantiagoCantidad, int) or SantiagoCantidad <= 0:
            raise ValueError("La cantidad a añadir debe ser un número entero positivo.")
        SantiagoProducto = SantiagoProducto.strip().lower()
        self.santiago_items[SantiagoProducto] = self.santiago_items.get(SantiagoProducto, 0) + SantiagoCantidad
        return f"Añadidos {SantiagoCantidad} de '{SantiagoProducto}'. Total: {self.santiago_items[SantiagoProducto]}."

    def SantiagoRemoveItem(self, SantiagoProducto, SantiagoCantidad):
        if not isinstance(SantiagoProducto, str) or not SantiagoProducto.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        if not isinstance(SantiagoCantidad, int) or SantiagoCantidad <= 0:
            raise ValueError("La cantidad a eliminar debe ser un número entero positivo.")
        SantiagoProducto = SantiagoProducto.strip().lower()
        if SantiagoProducto not in self.santiago_items:
            raise ValueError(f"El producto '{SantiagoProducto}' no existe en el inventario.")
        if self.santiago_items[SantiagoProducto] < SantiagoCantidad:
            raise ValueError(f"Solo hay {self.santiago_items[SantiagoProducto]} de '{SantiagoProducto}'. No se pueden eliminar {SantiagoCantidad}.")
        
        self.santiago_items[SantiagoProducto] -= SantiagoCantidad
        if self.santiago_items[SantiagoProducto] == 0:
            del self.santiago_items[SantiagoProducto]
            return f"Eliminados {SantiagoCantidad} de '{SantiagoProducto}'. Producto agotado y removido."
        else:
            return f"Eliminados {SantiagoCantidad} de '{SantiagoProducto}'. Restantes: {self.santiago_items[SantiagoProducto]}."

    def SantiagoGetQuantity(self, SantiagoProducto):
        if not isinstance(SantiagoProducto, str) or not SantiagoProducto.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        SantiagoProducto = SantiagoProducto.strip().lower()
        return self.santiago_items.get(SantiagoProducto, 0)

    def SantiagoListItems(self):
        if not self.santiago_items:
            return "El inventario está vacío."
        items_list = "\n".join([f"- {prod.capitalize()}: {qty}" for prod, qty in self.santiago_items.items()])
        return f"Inventario actual:\n{items_list}"

    def __str__(self):
        return self.SantiagoListItems()


try:
    santiagoTienda1 = SantiagoBInv()
    print(santiagoTienda1)

    print(santiagoTienda1.SantiagoAddItem("Tomates", 80))
    print(santiagoTienda1.SantiagoAddItem("Jugo de Naranja", 40))
    print(santiagoTienda1.SantiagoAddItem("Tomates", 25))  
    print(santiagoTienda1)

    print(f"Cantidad de Tomates: {santiagoTienda1.SantiagoGetQuantity('Tomates')}")
    print(f"Cantidad de Pan Integral: {santiagoTienda1.SantiagoGetQuantity('Pan Integral')}")  

    print(santiagoTienda1.SantiagoRemoveItem("Jugo de Naranja", 15))
    print(santiagoTienda1.SantiagoRemoveItem("Tomates", 105))  # Agota los tomates
    print(santiagoTienda1)

except ValueError as e:
    print(f"Error de inventario: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
