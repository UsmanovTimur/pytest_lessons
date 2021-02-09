import pytest
from .exp5 import exp5


@pytest.mark.parametrize("input_d,expected_output", [
    (2, True),
    (3, False),
    (27, False),
])
def test_normal_exp5(input_d, expected_output):
    result = exp5(input_d)
    print("input: {0}, output: {1}, expected: {2}".format(input_d, result, expected_output))
    assert result == expected_output
