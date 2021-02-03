import pytest
from .sum_int import sum


def test_normal_sum_int():
    assert sum(1, 5) == 6


def test_string_sum_int():
    assert sum("1", 5) is None


@pytest.fixture(params=[
    ((1, 2), 3),
    ((2, 3), 5),
])
def param_test(request):
    print(111, request.fixturename)
    return request.param


def test_normal_sum_int2(param_test):
    (input_d, expected_output) = param_test
    result = sum(input_d[0], input_d[1])
    print("input: {0}, output: {1}, expected: {2}".format(input_d, result, expected_output))
    assert result == expected_output
