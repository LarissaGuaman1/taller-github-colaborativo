class Producto:
    def __init__(self, nombre: str, precio: float, stock: int):
        if not nombre.strip():
            raise ValueError("El nombre es obligatorio")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero")

        if stock < 0:
            raise ValueError("El stock no puede ser negativo")

        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def agregar_stock(self, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")

        self.stock += cantidad

    def vender(self, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")

        if cantidad > self.stock:
            raise ValueError("Stock insuficiente")

        self.stock -= cantidad
        return self.precio * cantidad