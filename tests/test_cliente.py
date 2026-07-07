import pytest

from src.cliente import Cliente


def test_crear_cliente():
    cliente = Cliente("María", "maria@email.com")

    assert cliente.nombre == "María"
    assert cliente.correo == "maria@email.com"


def test_registrar_compra():
    cliente = Cliente("Juan", "juan@email.com")

    cliente.registrar_compra("Teclado")
    cliente.registrar_compra("Mouse")

    assert cliente.total_compras() == 2


def test_rechazar_correo_invalido():
    with pytest.raises(ValueError, match="correo"):
        Cliente("Pedro", "correo-invalido") 