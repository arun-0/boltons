import copy
import pickle

from boltons.typeutils import make_sentinel, typename

NOT_SET = make_sentinel('not_set', var_name='NOT_SET')

def test_sentinel_falsiness():
    assert not NOT_SET


def test_sentinel_pickle():
    assert pickle.dumps(NOT_SET)

def test_sentinel_copy():
    test = make_sentinel('test')
    assert test is copy.copy(test)
    assert test is copy.deepcopy(test)


def test_typename_builtins():
    assert typename(1) == 'int'
    assert typename('hello') == 'str'
    assert typename([]) == 'list'
    assert typename({}) == 'dict'
    assert typename(()) == 'tuple'
    assert typename(1.0) == 'float'
    assert typename(True) == 'bool'


def test_typename_none():
    assert typename(None) == 'NoneType'


def test_typename_custom_class_instance():
    class MyClass:
        pass

    assert typename(MyClass()) == 'MyClass'


def test_typename_custom_class_itself():
    class MyClass:
        pass

    # typename(MyClass) looks at type(MyClass), which is `type` for an
    # ordinary class, not the class's own name.
    assert typename(MyClass) == 'type'
