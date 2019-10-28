# test filename begins with 'test_'

import inc_dec # the filename of code being tested

def test_increment():  # name of specific test = test_functionname
    assert inc_dec.increment(3) == 4  # assert code_filename.functionname(input) = expectedresult

def test_decrement():
    assert inc_dec.decrement(3) == 4