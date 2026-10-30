import copy
import pickle

from boltons.typeutils import make_sentinel, typename

NOT_SET = make_sentinel('not_set', var_name='NOT_SET')


def test_typename():
    class Example:
        pass

    assert typename(1) == 'int'
    assert typename(Example()) == 'Example'


def test_sentinel_falsiness():
    assert not NOT_SET


def test_sentinel_pickle():
    assert pickle.dumps(NOT_SET)

def test_sentinel_copy():
    test = make_sentinel('test')
    assert test is copy.copy(test)
    assert test is copy.deepcopy(test)
