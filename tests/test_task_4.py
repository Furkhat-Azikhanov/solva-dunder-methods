from tasks import CustomList


def test_customlist():
    cl = CustomList([1, 2, 3])
    assert len(cl) == 3
    assert cl[1] == 2
    assert 3 in cl
    assert 4 not in cl
