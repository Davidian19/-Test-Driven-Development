from aula_1.src.incrementador import *
import pytest


@pytest.mark.parametrize("a, resp_esp", [(2,3),(3,4)])
def test_incre(a, resp_esp):
    i = Incrementador()
    res = i.inc(a) #chamando objeto da classe e a função
    assert res == resp_esp



@pytest.mark.parametrize("a", [(2.1),(-2),(4.12),("d")])
def test_incre_natural(a):
    i = Incrementador()
    with pytest.raises(IncError):
        res = i.inc(a)


def test_incre_mult():
    i = Incrementador()
    list = [1, 2, 3]
    res = i.inc(list)
    assert res == [2, 3, 4]