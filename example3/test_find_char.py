import pytest
from .find_char import find


@pytest.mark.parametrize("input_d,expected_output", [
    (("aaabbbccc", "a"), 0),
    (("aaabbbccc", "c"), 6),
    (("aaabbbccc", "d"), -1),
])
def test_normal_sum_int2(input_d, expected_output):
    result = find(input_d[0], input_d[1])
    print("input: {0}, output: {1}, expected: {2}".format(input_d, result, expected_output))
    assert result == expected_output


from .self_work import split


@pytest.mark.parametrize("input_d,expected_output", [
    (("Hello world!!!", " "), ['Hello', 'world!!!']),
    (("Helloworld!!! ", " "), ['Helloworld!!!', '']),
])
def test_normal_sum_int2(input_d, expected_output):
    result = split(input_d[0], input_d[1])
    print("input: {0}, output: {1}, expected: {2}".format(input_d, result, expected_output))
    assert result == expected_output
