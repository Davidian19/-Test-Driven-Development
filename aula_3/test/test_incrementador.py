from aula_3.src.incrementador import *
import pytest

@pytest.mark.parametrize("a, resp_esp", [([2, 3], []),
                                         ([1], []),
                                         ([1, 2, 3, 4, 5], [2, 3, 4]),
                                         ([1, 1.5, 2, 2.5],[1.5, 2] ),
                                         ([], [])
                                        ])
def test_value(a, resp_esp):
    i = Change()
    res = i.troca(a)
    assert res == resp_esp

@pytest.mark.parametrize("a", [ ( 's' ) ] )
def test_noList(a):
    i = Change()
    res = i.troca(a)
    assert res

@pytest.mark.parametrize("a, resp_esp", [([2, 'n'], [2, 'n'])] )
def test_stringList(a, resp_esp):
    i = Change()
    res = i.troca(a)
    assert res == resp_esp
