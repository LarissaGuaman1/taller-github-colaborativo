import pytest

from src.producto import Producto


def test_crear_producto():
    producto = Producto("Teclado", 25.50, 10)

    assert producto.nombre == "Teclado"
    assert producto.precio == 25.50
    assert producto.stock == 10


def test_agregar_stock():
    producto = Producto("Mouse", 15, 5)

    producto.agregar_stock(3)

    assert producto.stock == 8


def test_vender_producto():
    producto = Producto("Monitor", 180, 4)

    total = producto.vender(2)

    assert producto.stock == 2
    assert total == 360


def test_rechazar_venta_sin_stock():
    producto = Producto("Laptop", 850, 1)

    with pytest.raises(ValueError, match="Stock insuficiente"):
        producto.vender(2)