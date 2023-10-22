import pytest
from src.actividad1 import crear_repeticiones
@pytest.mark.parametrize(
    "nombre, numero, repeticiones",
    [
        ("cesar",10,"cesar\ncesar\ncesar\ncesar\ncesar\ncesar\ncesar\ncesar\ncesar\ncesar\n")
    ]  
)
def test_crear_repeticiones_params(nombre,numero,repeticiones):
    assert crear_repeticiones(nombre,numero,) == repeticiones