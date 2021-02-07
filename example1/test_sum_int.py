import pytest
from .sum_int import sum


def test_normal_sum_int():
    assert sum(1, 5) == 6


def test_string_sum_int():
    assert sum("1", 5) is None


@pytest.mark.parametrize("input_d,expected_output", [
    ((1, 2), 3),
    ((2, 3), 5),
    ((-2, 3), 1),
])
def test_normal_sum_int2(input_d, expected_output):
    result = sum(input_d[0], input_d[1])
    print("input: {0}, output: {1}, expected: {2}".format(input_d, result, expected_output))
    assert result == expected_output
