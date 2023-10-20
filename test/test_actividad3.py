import pytest
from src.actividad3 import crear_impares
@pytest.mark.parametrize(
    #valores
    "numero, impares",
    [
        #lo que queremos escribir
        (21,"1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21")
    ]  
)
#valores
def test_crear_impares_params(numero, impares):
    #la funcion de procesamiento y el valor que devuelve
    assert crear_impares(numero) == impares