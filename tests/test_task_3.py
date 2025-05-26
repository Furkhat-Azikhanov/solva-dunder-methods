from tasks import Temperature


def test_temperature():
    t1 = Temperature(25)
    t2 = Temperature(10)
    t3 = t1 + t2
    assert isinstance(float(t1), float)
    assert repr(t1) == 'Temperature(25°C)'
    assert t3 == Temperature(35)