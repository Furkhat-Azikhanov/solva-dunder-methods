from tasks import Circle


def test_circle():
    c1 = Circle(5)
    c2 = Circle(3)
    assert str(c1) == 'Circle with radius: 5'
    assert (c2 < c1) is True
    c3 = c1 * 2
    assert c3.radius == 10
