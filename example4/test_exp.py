import pytest
from .exp import sub


@pytest.mark.parametrize("input_d,expected_output", [
    ((2, 4), 0.5),
    ((4, 2), 2),
    ((9, 3), 3),
])
def test_normal_sub(input_d, expected_output):
    result = sub(input_d[0], input_d[1])
    print("input: {0}, output: {1}, expected: {2}".format(input_d, result, expected_output))
    assert result == expected_output


@pytest.mark.parametrize("input_d,exceptions", [
    ((2, 0), ZeroDivisionError),
    (("2", 0), TypeError),
])
def test_exceptions(input_d, exceptions):
    with pytest.raises(exceptions):
        result = sub(input_d[0], input_d[1])
