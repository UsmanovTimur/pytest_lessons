from .mult_arr import mult_arr


def test_normal_sum_int():
    assert mult_arr([1, 5]) == [2, 10]


def test_string_sum_int():
    assert mult_arr(112233) is None
