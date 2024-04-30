from datetime import date
from kakebo import Ingreso
import pytest

def test_instanciar_ingresos():
    movimiento = Ingreso("Loteria", date(2024, 1, 5), 1000)

    assert movimiento.concepto == "Loteria"
    assert movimiento.fecha == date(2024, 1, 5)
    assert movimiento.cantidad == 1000

def test_ingreso_concepto_debe_ser_str():
    with pytest.raises(TypeError):
       movimiento = Ingreso(19, date(2024, 1, 5), 1000)

def test_ingreso_fecha_debe_ser_date():
    with pytest.raises(TypeError):
       movimiento = Ingreso("Loteria", "goggooogl", 1000)

def test_ingreso_cantidad_debe_ser_num():
    with pytest.raises(TypeError):
        movimiento = Ingreso("Loteria", date.today(), "lola")
    movimiento = Ingreso("Loteria", date(2024, 1, 5), 1000)
    movimiento = Ingreso("Loteria", date(2024, 1, 5), 1000.1)