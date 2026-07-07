import re


class Cliente:
    def __init__(self, nombre: str, correo: str):
        if not nombre.strip():
            raise ValueError("El nombre es obligatorio")

        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if not re.match(patron, correo):
            raise ValueError("El correo no es válido")

        self.nombre = nombre
        self.correo = correo
        self.compras = []

    def registrar_compra(self, producto: str):
        if not producto.strip():
            raise ValueError("El producto es obligatorio")

        self.compras.append(producto)

    def total_compras(self):
        return len(self.compras)