from tasks import Vector2D


def test_vector2d():
    v1 = Vector2D(1, 2)
    v2 = Vector2D(3, 4)
    v3 = v1 + v2
    assert repr(v1) == 'Vector2D(1, 2)'
    assert v3 == Vector2D(4, 6)
    assert v1 != v2
