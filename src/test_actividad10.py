import pytest
from src.actividad10 import indicar_numeroprimo
@pytest.mark.parametrize(
    "numero, primo, noprimo",
    [
        (2," es primo"),
        (9," no es primo")
    ]  
)
def test_indicar_numeroprimo_params(numero,primo,noprimo):
    assert indicar_numeroprimo(numero) == primo
    assert indicar_numeroprimo(numero)==noprimo
