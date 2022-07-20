from aula_2.src.incrementador import *
import pytest

@pytest.mark.parametrize("a, resp_esp", [ ( [ 2, 3 ], [ 3, 2 ] ),
                                          ([ 2, 3, 4, 5 ], [3, 4, 5, 2]),
                                          ([1, 'a', 2, 'b' ], ['a', 2, 'b', 1])
                                          ] )
def test_acept(a, resp_esp):
    i = Change()
    res = i.troca(a)
    assert res == resp_esp

@pytest.mark.parametrize("a, resp_esp", [ ( [2], [2] ) ] )
def test_oneItem(a, resp_esp):
    i = Change()
    res = i.troca(a)
    assert res == resp_esp

@pytest.mark.parametrize("a, resp_esp", [ ( ['a', 'b', 'c'], ['b', 'c', 'a'] ) ] )
def test_char(a, resp_esp):
    i = Change()
    res = i.troca(a)
    assert res == resp_esp

@pytest.mark.parametrize("a", [ ('a') ] )
def test_noList(a):
    i = Change()
    res = i.troca(a)
    res

@pytest.mark.parametrize("a, resp_esp", [ ( [], [] ) ] )
def test_novalue(a, resp_esp):
    i = Change()
    res = i.troca(a)
    assert res == resp_esp