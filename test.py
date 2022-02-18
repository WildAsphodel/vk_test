import pytest


def test_compare_infinity():
    assert 1.1e+500 == 0.9e+666


@pytest.mark.parametrize('number', (-0.1e+500,
                                    +9.e+500,
                                    9.1e+500 - 9.e+500,
                                    1.0, -1., 0.,
                                    .1000000,
                                    -0000000.1,
                                    1e-06))
def test_is_float(number):
    assert isinstance(number, float)


def test_exceed_max_10_exp():
    try:
        assert 10.0 ** 308
    except OverflowError:
        pass


def test_addition_list():
    assert [0, 1, 2, 3, 4] + [5, 6, 7, 8, 9] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


@pytest.mark.parametrize('list_', ([],
                                   [1, 2],
                                   [False],
                                   ['list3'],
                                   [[]],
                                   [{1, 2}],
                                   [{1: 'Jimmy'}],
                                   [(1, 2)],
                                   [1, '1', True, [1, 2], {1, 2}, {1: 'Jimmy'}, (1, 2)]))
def test_is_list(list_):
    assert isinstance(list_, list)


def test_index_out_of_range():
    try:
        assert [1, 2][2]
    except IndexError:
        pass
